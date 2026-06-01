# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/99?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/99
- Title: Raising awareness and encouraging the prevention of stalking by designating January 2025 as "National Stalking Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 99
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-04-01T13:45:55Z
- Update date including text: 2026-04-01T13:45:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-04 - Committee: Submitted in House
- Latest action: 2025-02-04: Submitted in House

## Actions

- 2025-02-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-04 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/99",
    "number": "99",
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
    "title": "Raising awareness and encouraging the prevention of stalking by designating January 2025 as \"National Stalking Awareness Month\".",
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
      "actionDate": "2025-02-04",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-04T17:04:40Z",
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
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres99ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 99\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Fitzpatrick (for himself and Mrs. Dingell ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRaising awareness and encouraging the prevention of stalking by designating January 2025 as National Stalking Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\ndesignates National Stalking Awareness Month ;\n**(2)**\napplauds the efforts of service providers, police departments, prosecutor's offices, national and community organizations, colleges and universities, and private sector entities that combat stalking, support victims, and bring awareness to this crime;\n**(3)**\nencourages policymakers, criminal justice officials, victim service and human service agencies, institutions of higher education, and nonprofit organizations to increase awareness of stalking and continue to support the availability of services for victims of stalking; and\n**(4)**\nurges national and community organizations, businesses in the private sector, and the media to promote awareness of the crime of stalking through National Stalking Awareness Month .",
      "versionDate": "2025-02-04",
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-27",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1021",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Raising awareness and encouraging the prevention of stalking by designating January 2026 as \"National Stalking Awareness Month\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-21",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1303; text: CR S1136)"
      },
      "number": "88",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating March 7, 2025, as \"National Speech and Debate Education Day\".",
      "type": "SRES"
    },
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
            "name": "Assault and harassment offenses",
            "updateDate": "2025-02-10T18:23:46Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-02-10T18:23:46Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-02-10T18:23:46Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-02-10T18:23:46Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-02-10T18:23:46Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-02-10T18:23:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-07T14:01:29Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres99ih.xml"
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
      "title": "Raising awareness and encouraging the prevention of stalking by designating January 2025 as \"National Stalking Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T12:03:26Z"
    },
    {
      "title": "Raising awareness and encouraging the prevention of stalking by designating January 2025 as \"National Stalking Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T09:06:41Z"
    }
  ]
}
```
