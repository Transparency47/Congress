# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/831?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/831
- Title: Expressing support for the designation of October 2025 as "National Down Syndrome Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 831
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2025-12-03T16:58:06Z
- Update date including text: 2025-12-03T16:58:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-10-24 - IntroReferral: Submitted in House
- 2025-10-24 - IntroReferral: Submitted in House
- Latest action: 2025-10-24: Submitted in House

## Actions

- 2025-10-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-10-24 - IntroReferral: Submitted in House
- 2025-10-24 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/831",
    "number": "831",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Expressing support for the designation of October 2025 as \"National Down Syndrome Awareness Month\".",
    "type": "HRES",
    "updateDate": "2025-12-03T16:58:06Z",
    "updateDateIncludingText": "2025-12-03T16:58:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NJ"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres831ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 831\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Mr. Garbarino (for himself and Mr. Gottheimer ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of October 2025 as National Down Syndrome Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National Down Syndrome Awareness Month ;\n**(2)**\nbelieves National Down Syndrome Awareness Month is an opportunity to celebrate people with Down syndrome and their families as they continue to advocate for access and opportunity to live fully included lives;\n**(3)**\ncommends people with Down syndrome, their families, medical researchers, doctors, scientists, and organizations who are the driving force behind improving the quality of life for people with Down syndrome; and\n**(4)**\nreiterates its commitment to ensuring Federal investment into Down syndrome research and pursuing policies to better support the Down syndrome community.",
      "versionDate": "2025-10-24",
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
        "updateDate": "2025-12-03T16:58:06Z"
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
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres831ih.xml"
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
      "title": "Expressing support for the designation of October 2025 as \"National Down Syndrome Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T04:18:15Z"
    },
    {
      "title": "Expressing support for the designation of October 2025 as \"National Down Syndrome Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-25T08:05:46Z"
    }
  ]
}
```
