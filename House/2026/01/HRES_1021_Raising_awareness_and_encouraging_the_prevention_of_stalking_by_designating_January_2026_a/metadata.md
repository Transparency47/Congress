# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1021
- Title: Raising awareness and encouraging the prevention of stalking by designating January 2026 as "National Stalking Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1021
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-04-01T13:45:55Z
- Update date including text: 2026-04-01T13:45:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-27 - IntroReferral: Submitted in House
- 2026-01-27 - IntroReferral: Submitted in House
- Latest action: 2026-01-27: Submitted in House

## Actions

- 2026-01-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-27 - IntroReferral: Submitted in House
- 2026-01-27 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1021",
    "number": "1021",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Raising awareness and encouraging the prevention of stalking by designating January 2026 as \"National Stalking Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-04-01T13:45:55Z",
    "updateDateIncludingText": "2026-04-01T13:45:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:31:40Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1021ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1021\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Fitzpatrick (for himself and Mrs. Dingell ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRaising awareness and encouraging the prevention of stalking by designating January 2026 as National Stalking Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\ndesignates National Stalking Awareness Month ;\n**(2)**\napplauds the efforts of service providers, police departments, prosecutor's offices, national and community organizations, colleges and universities, and private sector entities that combat stalking, support victims, and bring awareness to this crime;\n**(3)**\nencourages policymakers, criminal justice officials, victim service and human service agencies, institutions of higher education, and nonprofit organizations to increase awareness of stalking and continue to support the availability of services for victims of stalking; and\n**(4)**\nurges national and community organizations, businesses in the private sector, and the media to promote awareness of the crime of stalking through National Stalking Awareness Month .",
      "versionDate": "2026-01-27",
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
        "actionDate": "2025-01-29",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S488; text: CR S487)"
      },
      "number": "46",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution raising awareness and encouraging the prevention of stalking by designating January 2025 as \"National Stalking Awareness Month\".",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "99",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Raising awareness and encouraging the prevention of stalking by designating January 2025 as \"National Stalking Awareness Month\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-09",
        "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S537; text: CR 1/27/2026 S293-294)"
      },
      "number": "586",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution raising awareness and encouraging the prevention of stalking by designating January 2026 as \"National Stalking Awareness Month\".",
      "type": "SRES"
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
        "updateDate": "2026-02-02T14:33:31Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1021ih.xml"
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
      "title": "Raising awareness and encouraging the prevention of stalking by designating January 2026 as \"National Stalking Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:18:22Z"
    },
    {
      "title": "Raising awareness and encouraging the prevention of stalking by designating January 2026 as \"National Stalking Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T09:05:32Z"
    }
  ]
}
```
