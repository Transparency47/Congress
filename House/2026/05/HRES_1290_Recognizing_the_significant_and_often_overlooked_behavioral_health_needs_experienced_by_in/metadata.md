# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1290?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1290
- Title: Recognizing the significant and often overlooked behavioral health needs experienced by individuals and families affected by rare diseases, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 1290
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-29T16:07:43Z
- Update date including text: 2026-05-29T16:07:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-14 - IntroReferral: Submitted in House
- Latest action: 2026-05-14: Submitted in House

## Actions

- 2026-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1290",
    "number": "1290",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000469",
        "district": "20",
        "firstName": "Paul",
        "fullName": "Rep. Tonko, Paul [D-NY-20]",
        "lastName": "Tonko",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Recognizing the significant and often overlooked behavioral health needs experienced by individuals and families affected by rare diseases, and for other purposes.",
    "type": "HRES",
    "updateDate": "2026-05-29T16:07:43Z",
    "updateDateIncludingText": "2026-05-29T16:07:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T14:03:35Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1290ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1290\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2026 Mr. Tonko (for himself and Mr. Bacon ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the significant and often overlooked behavioral health needs experienced by individuals and families affected by rare diseases, and for other purposes.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the significant and often overlooked behavioral health needs experienced by individuals and families affected by rare diseases;\n**(2)**\naffirms that behavioral health care is an essential component of comprehensive rare disease care and should be integrated into clinical pathways, research agendas, and Federal policies;\n**(3)**\ncalls upon Federal agencies, including the Department of Health and Human Services, the National Institutes of Health, and the Centers for Medicare & Medicaid Services, to prioritize behavioral health access within rare disease initiatives, research funding, and care delivery models;\n**(4)**\nencourages the development and expansion of standardized, evidence-informed peer support programs for rare disease patients, caregivers, and families, including support for virtual and community-based models;\n**(5)**\nsupports efforts to strengthen cultural competency and cultural humility across the behavioral health and rare disease workforce, including training, community partnerships, and equitable access initiatives;\n**(6)**\nurges investment in the behavioral health workforce, particularly child and adolescent providers, to ensure adequate capacity to meet the needs of rare disease families;\n**(7)**\nrecommends that public and private payors evaluate and address reimbursement barriers that limit access to integrated behavioral health services for rare disease patients;\n**(8)**\nencourages the creation of Federal incentives for clinicians to pursue continuing medical education on rare diseases, including their psychiatric and psychosocial dimensions; and\n**(9)**\nsupports ongoing collaboration among Federal agencies, patient advocacy organizations, academic institutions, and community partners to develop comprehensive strategies that address the behavioral health needs of the rare disease community.",
      "versionDate": "2026-05-14",
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
        "updateDate": "2026-05-29T16:07:43Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1290ih.xml"
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
      "title": "Recognizing the significant and often overlooked behavioral health needs experienced by individuals and families affected by rare diseases, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:18:28Z"
    },
    {
      "title": "Recognizing the significant and often overlooked behavioral health needs experienced by individuals and families affected by rare diseases, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:07:34Z"
    }
  ]
}
```
