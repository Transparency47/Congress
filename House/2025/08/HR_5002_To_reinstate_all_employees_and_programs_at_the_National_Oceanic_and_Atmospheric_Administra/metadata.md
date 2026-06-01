# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5002?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5002
- Title: Protect Americans from Climate Disasters Act
- Congress: 119
- Bill type: HR
- Bill number: 5002
- Origin chamber: House
- Introduced date: 2025-08-19
- Update date: 2025-10-09T08:05:58Z
- Update date including text: 2025-10-09T08:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-19: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-19 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-19: Introduced in House

## Actions

- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-19 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-19",
    "latestAction": {
      "actionDate": "2025-08-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5002",
    "number": "5002",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Protect Americans from Climate Disasters Act",
    "type": "HR",
    "updateDate": "2025-10-09T08:05:58Z",
    "updateDateIncludingText": "2025-10-09T08:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-19",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-19",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-08-19T14:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-19T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "TX"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "AZ"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "RI"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "OR"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "TN"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "OR"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "AZ"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "DC"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "IL"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5002ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5002\nIN THE HOUSE OF REPRESENTATIVES\nAugust 19, 2025 Mr. Neguse (for himself, Mr. Casar , Mr. Stanton , Mr. Amo , Ms. Hoyle of Oregon , and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reinstate all employees and programs at the National Oceanic and Atmospheric Administration that help communities prepare for and mitigate damage from extreme weather events.\n#### 1. Short title\nThis Act may be cited as the Protect Americans from Climate Disasters Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Fifth United States National Climate Assessment reported that human-caused climate variability such as extended droughts, longer wildfire seasons, heavy rainfall, and sea level rise affects the frequency and intensity of extreme weather events.\n**(2)**\nAccording to the National Oceanic and Atmospheric Administration (NOAA), the number and cost of extreme weather and climate disasters have increased over time and will continue to increase in the United States due to climate change, increased urbanization, and development in weather prone areas.\n**(3)**\nAccording to the National Centers for Environmental Information, from 2020 to 2024 alone, weather and climate disasters cost the United States over $746,700,000,000 and led to 2,520 deaths.\n**(4)**\nAmericans rely on weather information provided by NOAA every day for emergency disaster alerts, forecasting, data collection, and more.\n**(5)**\nStaffing reductions at the National Weather Service and NOAA have resulted in decreased capacity to forecast extreme weather events, the elimination of some products and services, and the deterioration of environmental scientific research, which poses a threat to public safety.\n**(6)**\nThe 5 former living National Weather Service leaders wrote an open letter expressing their deep concern that the staff and program cuts at NOAA may result in the loss of life.\n**(7)**\nNOAA\u2019s Billion-Dollar Weather and Climate Disasters product has been eliminated, reducing publicly available data that tracked the economic impact of United States weather and climate trends since 1980.\n#### 3. Definition\nIn this Act, the term NOAA means the National Oceanic and Atmospheric Administration.\n#### 4. NOAA staffing and personnel\nNot later than 30 days after the date of enactment of this Act, using funds previously appropriated for such purposes, the Secretary of Commerce shall\u2014\n**(1)**\ntake such actions as are necessary to ensure that NOAA, including the National Weather Service, is fully staffed to ensure timely and accurate data, forecasts, weather alerts, and resiliency resources are available to prepare for extreme weather events; and\n**(2)**\nreinstate any individuals who\u2014\n**(A)**\nwere involuntarily removed or otherwise terminated from employment with NOAA during the period beginning on January 20, 2025, and ending on the date of the enactment of this Act; and\n**(B)**\nelect to be reinstated.\n#### 5. Continuation of authorized NOAA programs\n##### (a) Requirements\nThe Secretary of Commerce\u2014\n**(1)**\nshall continue to carry out any programs for which funds have been appropriated that support State and local efforts to prepare for and respond to extreme weather events; and\n**(2)**\nmay not make any changes to existing congressionally mandated programs that will reduce access to extreme weather resources.\n##### (b) Actions required\nIn carrying out subsection (a)\u2014\n**(1)**\nthe Secretary of Commerce shall immediately reinstate the Billion-Dollar Weather and Climate Disasters product and carry out any project for which funds have been made available under such program;\n**(2)**\nthe Secretary of Commerce shall immediately reinstate the NOAA Marine Environmental Buoy Database and carry out any project for which funds have been made available under such program; and\n**(3)**\nthe Secretary of Commerce shall immediately reinstate the NOAA Global Ocean Currents Database and carry out any project for which funds have been made available under such program.\n#### 6. National Oceanic And Atmospheric Administration funding\nThere is appropriated to the Department of Commerce, out of any money in the Treasury not otherwise appropriated, for the fiscal year ending on September 30, 2026, $6,756,300,000 for the necessary expenses of National Oceanic and Atmospheric Administration.",
      "versionDate": "2025-08-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Emergency Management",
        "updateDate": "2025-09-19T15:52:31Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5002ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reinstate all employees and programs at the National Oceanic and Atmospheric Administration that help communities prepare for and mitigate damage from extreme weather events.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-20T10:08:17Z"
    },
    {
      "title": "Protect Americans from Climate Disasters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-20T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Americans from Climate Disasters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-20T08:23:16Z"
    }
  ]
}
```
