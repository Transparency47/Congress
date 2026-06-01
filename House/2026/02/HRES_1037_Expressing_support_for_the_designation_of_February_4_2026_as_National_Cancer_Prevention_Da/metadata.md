# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1037?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1037
- Title: Expressing support for the designation of February 4, 2026, as "National Cancer Prevention Day".
- Congress: 119
- Bill type: HRES
- Bill number: 1037
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-03-30T21:22:12Z
- Update date including text: 2026-03-30T21:22:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-04 - IntroReferral: Submitted in House
- 2026-02-04 - IntroReferral: Submitted in House
- Latest action: 2026-02-04: Submitted in House

## Actions

- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-04 - IntroReferral: Submitted in House
- 2026-02-04 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1037",
    "number": "1037",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Expressing support for the designation of February 4, 2026, as \"National Cancer Prevention Day\".",
    "type": "HRES",
    "updateDate": "2026-03-30T21:22:12Z",
    "updateDateIncludingText": "2026-03-30T21:22:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:00:35Z",
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
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1037ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1037\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mrs. Dingell (for herself and Mr. James ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of February 4, 2026, as National Cancer Prevention Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Cancer Prevention Day ;\n**(2)**\nrecognizes all efforts to raise the awareness for the reduction of cancer risks; and\n**(3)**\nrecognizes the devastating effect cancer has on families and wishes to expand knowledge, encourage early detection, and work with friends in the medical and scientific fields to put an end to this deadly disease.",
      "versionDate": "2026-02-04",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "98",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of February 4, 2025, as \"National Cancer Prevention Day\".",
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
        "updateDate": "2026-02-12T14:20:29Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1037ih.xml"
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
      "title": "Expressing support for the designation of February 4, 2026, as \"National Cancer Prevention Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T09:18:32Z"
    },
    {
      "title": "Expressing support for the designation of February 4, 2026, as \"National Cancer Prevention Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T09:06:21Z"
    }
  ]
}
```
