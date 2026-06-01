# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/451?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/451
- Title: A resolution condemning attacks on Federal law enforcement in the State of Illinois.
- Congress: 119
- Bill type: SRES
- Bill number: 451
- Origin chamber: Senate
- Introduced date: 2025-10-15
- Update date: 2025-12-05T15:50:01Z
- Update date including text: 2025-12-05T15:50:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-15: Introduced in Senate
- 2025-10-15 - IntroReferral: Introduced in Senate
- 2025-10-15 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S7140)
- Latest action: 2025-10-15: Introduced in Senate

## Actions

- 2025-10-15 - IntroReferral: Introduced in Senate
- 2025-10-15 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S7140)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-15",
    "latestAction": {
      "actionDate": "2025-10-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/451",
    "number": "451",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A resolution condemning attacks on Federal law enforcement in the State of Illinois.",
    "type": "SRES",
    "updateDate": "2025-12-05T15:50:01Z",
    "updateDateIncludingText": "2025-12-05T15:50:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S7140)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-10-15T19:03:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-15",
      "state": "TN"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "UT"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres451is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 451\nIN THE SENATE OF THE UNITED STATES\nOctober 15, 2025 Mr. Scott of Florida (for himself and Mrs. Blackburn ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCondemning attacks on Federal law enforcement in the State of Illinois.\nThat the Senate\u2014\n**(1)**\ncondemns all attacks on Federal law enforcement in the State of Illinois;\n**(2)**\nrecognizes that the State Government of Illinois and the city Government of Chicago have failed in their fundamental obligation to protect their residents from violent crime;\n**(3)**\ncommends the brave men and women of Federal law enforcement and all support personnel for their heroic work during this public safety crisis in Illinois;\n**(4)**\ncondemns any and all efforts by State or local governments, or by organized groups to obstruct, impede, or interfere with the lawful execution of Federal immigration law enforcement operations;\n**(5)**\ncondemns the implementation of pro-criminal prosecutorial policies that have contributed to the dramatic increase in violent crime in Chicago;\n**(6)**\ncondemns the prioritization of politics over the safety and well-being of Illinois residents, particularly those in vulnerable communities;\n**(7)**\nreaffirms the exclusive authority of the Federal Government to regulate immigration and to enforce immigration laws;\n**(8)**\nrecognizes that the Federal Government has a responsibility to protect all people of the United States from violent crime, particularly when State and local governments have abdicated this fundamental obligation through the implementation of failed criminal justice policies;\n**(9)**\nsupports all necessary measures to protect Federal law enforcement personnel and Federal facilities in Illinois from violent assault, intimidation, and obstruction;\n**(10)**\nsupports the prosecution, to the fullest extent of Federal law, of all individuals and groups who engage in violence, intimidation, or sabotage against Federal law enforcement; and\n**(11)**\nencourages all State and local governments to support and protect our brave Federal law enforcement officers and support staff.",
      "versionDate": "2025-10-15",
      "versionType": "IS"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-05T15:50:01Z"
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
      "date": "2025-10-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres451is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution condemning attacks on Federal law enforcement in the State of Illinois.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:03:16Z"
    },
    {
      "title": "A resolution condemning attacks on Federal law enforcement in the State of Illinois.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T10:56:16Z"
    }
  ]
}
```
