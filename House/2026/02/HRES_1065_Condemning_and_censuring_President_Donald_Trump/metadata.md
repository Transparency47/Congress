# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1065?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1065
- Title: Condemning and censuring President Donald Trump.
- Congress: 119
- Bill type: HRES
- Bill number: 1065
- Origin chamber: House
- Introduced date: 2026-02-13
- Update date: 2026-02-26T09:07:09Z
- Update date including text: 2026-02-26T09:07:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-13: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-13 - IntroReferral: Submitted in House
- 2026-02-13 - IntroReferral: Submitted in House
- Latest action: 2026-02-13: Submitted in House

## Actions

- 2026-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-13 - IntroReferral: Submitted in House
- 2026-02-13 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-13",
    "latestAction": {
      "actionDate": "2026-02-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1065",
    "number": "1065",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Condemning and censuring President Donald Trump.",
    "type": "HRES",
    "updateDate": "2026-02-26T09:07:09Z",
    "updateDateIncludingText": "2026-02-26T09:07:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-02-13T15:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1065ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1065\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2026 Mr. Cohen (for himself, Mr. Kennedy of New York , Mrs. Watson Coleman , and Mr. Green of Texas ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCondemning and censuring President Donald Trump.\nThat the House of Representatives\u2014\n**(1)**\ncensures and condemns President Donald Trump for his racist social media post of former President Barack Obama and First Lady Michelle Obama as primates made on February 5, 2026, which violates the President\u2019s oath of office to uphold and defend the Constitution; and\n**(2)**\ncalls on President Donald Trump to apologize for his repugnant social media post which have disgraced the Office of the President and dishonored the United States of America.",
      "versionDate": "2026-02-13",
      "versionType": "IH"
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-18T16:07:54Z"
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
      "date": "2026-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1065ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Condemning and censuring President Donald Trump.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-14T09:18:25Z"
    },
    {
      "title": "Condemning and censuring President Donald Trump.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-14T09:06:11Z"
    }
  ]
}
```
