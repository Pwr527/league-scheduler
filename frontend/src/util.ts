import axios, { AxiosResponse } from "axios"
import { useEffect, useState } from "react";
import { ApiResponse } from "./types";

export let config = {
    apiHost: process.env.REACT_APP_API_HOST + '/api/v1'
}

export async function createApiObject<T>(path: string, object: T) {
    let error: string | undefined
    let data: T | undefined
    let loading: boolean = true

    const sendPost = async () => {
        const url = config.apiHost + path
        await axios.post<T>(url, object)
            .then(response => {
                data = response.data
            })
            .catch(e => {
                error = e.message
            })
            .then(() => {
                loading = false
            })
    }
    await sendPost()
    return { data, loading, error };
}

export function useCreateApi<T>(path: string, object: T) {
    const [data, setData] = useState<T>();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const url = config.apiHost + path

    useEffect(() => {
        axios.post(url, object)
            .then(res => {
                const response:ApiResponse = res.data 
                if (response.error) setError(response.error)
                if (response.data) setData(response.data)
            })
            .catch(error => {
                setError(error)
            })
            .then(() => {
                setLoading(false)
            })

    }, [url]);

    return { data, loading, error };

}


export function useGetApi<T>(path: string) {
    const [data, setData] = useState<T>();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const url = config.apiHost + path

    useEffect(() => {
        axios.get(url)
            .then(res => {
                const response:ApiResponse = res.data 
                if (response.error) setError(response.error)
                if (response.data) setData(response.data)
            })
            .catch(error => {
                setError(error)
            })
            .then(() => {
                setLoading(false)
            })

    }, [url]);

    return { data, loading, error };
};
