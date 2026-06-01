# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1258
- Title: Expressing support for the designation of May 2026 as "National Brain Tumor Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1258
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-18T15:08:22Z
- Update date including text: 2026-05-18T15:08:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-04 - IntroReferral: Submitted in House
- Latest action: 2026-05-04: Submitted in House

## Actions

- 2026-05-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-04 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1258",
    "number": "1258",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "Q000023",
        "district": "5",
        "firstName": "Mike",
        "fullName": "Rep. Quigley, Mike [D-IL-5]",
        "lastName": "Quigley",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Expressing support for the designation of May 2026 as \"National Brain Tumor Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-05-18T15:08:22Z",
    "updateDateIncludingText": "2026-05-18T15:08:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
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
      "actionCode": "1025",
      "actionDate": "2026-05-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
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
          "date": "2026-05-04T14:32:35Z",
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
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "TX"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MA"
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
      "sponsorshipDate": "2026-05-07",
      "state": "DC"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1258ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1258\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Quigley (for himself and Mr. McCaul ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of May 2026 as National Brain Tumor Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National Brain Tumor Awareness Month ;\n**(2)**\nencourages increased public awareness of brain tumors to honor the individuals who have lost their lives to a brain tumor or currently live with a brain tumor diagnosis;\n**(3)**\nsupports efforts to develop better treatments for brain tumors that will improve the quality of life and the long-term prognosis of individuals diagnosed with a brain tumor;\n**(4)**\nexpresses its support for individuals who are battling brain tumors, as well as the families, friends, and caregivers of those individuals; and\n**(5)**\nurges a collaborative approach to brain tumor research, which is a promising means of advancing understanding of, and treatment for, brain tumors.",
      "versionDate": "2026-05-04",
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
        "actionDate": "2025-05-01",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "371",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of May 2025 as \"National Brain Tumor Awareness Month\".",
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
        "name": "Health",
        "updateDate": "2026-05-18T15:08:21Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1258ih.xml"
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
      "title": "Expressing support for the designation of May 2026 as \"National Brain Tumor Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T08:18:28Z"
    },
    {
      "title": "Expressing support for the designation of May 2026 as \"National Brain Tumor Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T08:06:09Z"
    }
  ]
}
```
