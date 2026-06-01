# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/485?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/485
- Title: Denouncing the antisemitic terrorist attack in Boulder, Colorado.
- Congress: 119
- Bill type: HRES
- Bill number: 485
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2025-06-24T13:48:10Z
- Update date including text: 2025-06-24T13:48:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-06 - IntroReferral: Submitted in House
- 2025-06-06 - IntroReferral: Submitted in House
- Latest action: 2025-06-06: Submitted in House

## Actions

- 2025-06-06 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-06 - IntroReferral: Submitted in House
- 2025-06-06 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/485",
    "number": "485",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Denouncing the antisemitic terrorist attack in Boulder, Colorado.",
    "type": "HRES",
    "updateDate": "2025-06-24T13:48:10Z",
    "updateDateIncludingText": "2025-06-24T13:48:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "CO"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "CO"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres485ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 485\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Evans of Colorado (for himself, Mr. Crank , Ms. Boebert , and Mr. Hurd of Colorado ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nDenouncing the antisemitic terrorist attack in Boulder, Colorado.\nThat the House of Representatives\u2014\n**(1)**\ncondemns Mohammed Sabry Soliman and his antisemitic terrorist attack on peaceful demonstrators supporting the release of the hostages held by Hamas;\n**(2)**\nprays for the quick healing of the victims of Mohammed Sabry Soliman\u2019s antisemitic terrorist attack;\n**(3)**\naffirms that free and open communication between State and local law enforcement and their Federal counterparts remains the bedrock of public safety and is necessary in preventing terrorist attacks; and\n**(4)**\nexpresses gratitude to law enforcement officers, including U.S. Immigration and Customs Enforcement personnel, for protecting the homeland.",
      "versionDate": "2025-06-06",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-09",
        "actionTime": "19:03:05",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "488",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Denouncing the antisemitic terrorist attack in Boulder, Colorado.",
      "type": "HRES"
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
        "updateDate": "2025-06-23T15:05:18Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres485ih.xml"
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
      "title": "Denouncing the antisemitic terrorist attack in Boulder, Colorado.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T08:48:18Z"
    },
    {
      "title": "Denouncing the antisemitic terrorist attack in Boulder, Colorado.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-07T08:06:18Z"
    }
  ]
}
```
