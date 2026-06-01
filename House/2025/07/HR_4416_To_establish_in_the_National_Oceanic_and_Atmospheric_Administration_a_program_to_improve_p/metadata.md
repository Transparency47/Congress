# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4416?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4416
- Title: To establish in the National Oceanic and Atmospheric Administration a program to improve precipitation forecasts, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 4416
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2025-09-12T17:55:47Z
- Update date including text: 2025-09-12T17:55:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4416",
    "number": "4416",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "R000305",
        "district": "2",
        "firstName": "Deborah",
        "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
        "lastName": "Ross",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "To establish in the National Oceanic and Atmospheric Administration a program to improve precipitation forecasts, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-09-12T17:55:47Z",
    "updateDateIncludingText": "2025-09-12T17:55:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
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
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4416ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4416\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Ms. Ross (for herself and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo establish in the National Oceanic and Atmospheric Administration a program to improve precipitation forecasts, and for other purposes.\n#### 1. Establishment of NOAA precipitation forecasts program\n##### (a) Establishment\nThere is established in the National Oceanic and Atmospheric Administration (NOAA) a program to improve precipitation forecasts (in this section referred to as the program ).\n##### (b) Goal\nThe goal of the program shall be to improve precipitation forecasts across all timescales through the research, development, and operational implementation of fully coupled Earth System Models. The program shall carry out the following:\n**(1)**\nImprove the understanding and prediction of precipitation extremes from a wide variety of weather systems and climate patterns.\n**(2)**\nImprove the development, production, management, assimilation, integration, availability, and curation of datasets for precipitation prediction.\n**(3)**\nIdentify and improve observations and analyses necessary for precipitation prediction, including relating to water vapor, oceans, and boundary layers.\n**(4)**\nUtilize high performance computing and other technologies, as appropriate, to advance Earth System Models predictions skill of precipitation extreme phenomena, including atmospheric rivers, tropical cyclones, and winter storms across weather, subseasonal, and decadal timescales.\n**(5)**\nAdvance understanding and modeling of precipitation processes key to improving models and precipitation forecasts from weather to subseasonal-to-seasonal (S2S) to seasonal-to-decadal (S2D) timescales.\n**(6)**\nSupport research and development to improve the accuracy, reliability, and timeliness of precipitation prediction, in collaboration with academic and private sector partners to test and evaluate emerging technologies, including the use of machine learning and artificial intelligence.\n**(7)**\nImprove weather, subseasonal, seasonal, and decadal skill for precipitation forecasts through the use of emerging techniques and technologies.\n**(8)**\nSupport research in social and behavioral sciences to improve precipitation forecast products and communication, in collaboration with the Director of the National Weather Service.\n**(9)**\nLead the ongoing advancement of current and next-generation precipitation forecasting models.\n**(10)**\nIdentify observational gaps, systematic errors, and model limitations in precipitation prediction systems.\n**(11)**\nImprove, expand, and sustain operational precipitation products and applications for decision support.\n**(12)**\nCoordinate across NOAA line offices to address priorities of the program.\n**(13)**\nDirect efforts to engage with Federal, State, local, Tribal, and academic entities and stakeholders, as appropriate, when conducting program activities.\n**(14)**\nEnsure adequate data management, access, and archive processes are in place to ensure data and metadata are findable, accessible, interoperable, and usable by the science community and public.\n##### (c) Updates\nThe Administrator of NOAA shall revise and update, as necessary, the goals of the program at least once every two years. Such revisions and updates shall be incorporated into relevant NOAA strategic implementation plans as determined appropriate by the Administrator.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to the National Oceanic and Atmospheric Administration to carry out this section the following:\n**(1)**\n$15,000,000 for fiscal year 2026.\n**(2)**\n$15,040,000 for fiscal year 2027.\n**(3)**\n$15,080,800 for fiscal year 2028.\n**(4)**\n$15,122,416 for fiscal year 2029.\n**(5)**\n$15,200,000 for fiscal year 2030.",
      "versionDate": "2025-07-15",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computers and information technology",
            "updateDate": "2025-09-12T17:55:06Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-09-12T17:55:47Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-12T17:39:10Z"
          },
          {
            "name": "Floods and storm protection",
            "updateDate": "2025-09-12T17:39:03Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-09-12T17:53:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-11T17:17:49Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4416ih.xml"
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
      "title": "To establish in the National Oceanic and Atmospheric Administration a program to improve precipitation forecasts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T11:48:20Z"
    },
    {
      "title": "To establish in the National Oceanic and Atmospheric Administration a program to improve precipitation forecasts, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:58Z"
    }
  ]
}
```
