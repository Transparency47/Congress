# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1044?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1044
- Title: Expressing support for the designation of the year 2026 as the "National Year of the Volunteer".
- Congress: 119
- Bill type: HRES
- Bill number: 1044
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-25T09:06:40Z
- Update date including text: 2026-02-25T09:06:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-02-09 - IntroReferral: Submitted in House
- 2026-02-09 - IntroReferral: Submitted in House
- Latest action: 2026-02-09: Submitted in House

## Actions

- 2026-02-09 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-02-09 - IntroReferral: Submitted in House
- 2026-02-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1044",
    "number": "1044",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Expressing support for the designation of the year 2026 as the \"National Year of the Volunteer\".",
    "type": "HRES",
    "updateDate": "2026-02-25T09:06:40Z",
    "updateDateIncludingText": "2026-02-25T09:06:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NJ"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NE"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1044ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1044\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Lawler (for himself, Mr. Moskowitz , Mrs. Watson Coleman , Mr. Aderholt , Ms. Salazar , and Mr. Evans of Pennsylvania ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for the designation of the year 2026 as the National Year of the Volunteer .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of the National Year of the Volunteer ;\n**(2)**\nhonors the millions of volunteers whose selfless service strengthens communities across the United States;\n**(3)**\nencourages Federal, State, and local efforts to highlight volunteer opportunities and drive public awareness of the value of service;\n**(4)**\nencourages nonprofit organizations, schools, veterans\u2019 groups, civic associations, and companies to partner and engage in volunteer opportunities across the United States; and\n**(5)**\ncalls on all Americans to celebrate the 250th anniversary of the United States, as the National Year of the Volunteer, by participating in acts of service and community improvement.",
      "versionDate": "2026-02-09",
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
        "name": "Health",
        "updateDate": "2026-02-18T19:29:52Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1044ih.xml"
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
      "title": "Expressing support for the designation of the year 2026 as the \"National Year of the Volunteer\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T10:18:26Z"
    },
    {
      "title": "Expressing support for the designation of the year 2026 as the \"National Year of the Volunteer\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T09:05:29Z"
    }
  ]
}
```
