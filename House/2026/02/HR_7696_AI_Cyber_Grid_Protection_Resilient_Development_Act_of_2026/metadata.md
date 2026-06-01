# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7696?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7696
- Title: AI Cyber Grid Protection Resilient Development Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7696
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-05-16T08:07:21Z
- Update date including text: 2026-05-16T08:07:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-26 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-26 - Committee: Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7696",
    "number": "7696",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001103",
        "district": "",
        "firstName": "Pablo",
        "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
        "lastName": "Hern\u00e1ndez",
        "party": "D",
        "state": "PR"
      }
    ],
    "title": "AI Cyber Grid Protection Resilient Development Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:21Z",
    "updateDateIncludingText": "2026-05-16T08:07:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Cybersecurity and Infrastructure Protection Subcommittee",
          "systemCode": "hshm08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Cybersecurity and Infrastructure Protection.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-02-25T14:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-26T20:55:16Z",
              "name": "Referred to"
            }
          },
          "name": "Cybersecurity and Infrastructure Protection Subcommittee",
          "systemCode": "hshm08"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7696ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7696\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Hern\u00e1ndez (for himself, Mr. Liccardo , and Mrs. Grijalva ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo establish a grant program to provide awards to National Laboratories and institutions of higher education to develop secure artificial intelligence (AI) cyber-physical testbeds to simulate grid-scale cyberattacks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI Cyber Grid Protection Resilient Development Act of 2026 .\n#### 2. Grant program to secure artificial intelligence (AI) cyber-physical testbeds to simulate grid-scale cyberattacks\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security and the Secretary of Homeland Security shall jointly establish a grant program to provide awards for each of fiscal years 2026 through 2030 to eligible entities to develop secure artificial intelligence (AI) cyber-physical testbeds to simulate grid-scale cyberattacks and train AI models safely.\n##### (b) Reports\nNot later than one year after the date of the enactment of this Act and annually thereafter through 2031, the Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security and the Secretary of Homeland Security shall jointly submit to Congress a report detailing evolving threats, AI mitigation progress, and recommendations for further legislative or regulatory action relating to grid-scale cyberattacks.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated $100,000,000 for fiscal years 2026 through 2030 to make grants under subsection (a).\n##### (d) Definitions\nIn this section:\n**(1) AI; artificial intelligence**\nThe terms AI and artificial intelligence have the meaning given the term artificial intelligence in section 238(g) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ).\n**(2) Eligible entity**\nThe term eligible entity means any of the following:\n**(A)**\nAn institution of higher education (as such term is defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )), including any of the following:\n**(i)**\nA public college or university.\n**(ii)**\nA community college.\n**(iii)**\nA Hispanic-serving institution (as such term is defined in section 502 of the Higher Education Act of 1965 ( 20 U.S.C. 1101a )).\n**(B)**\nA National Laboratory (as such term is defined in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 )).\n**(C)**\nA consortium comprised of one or more entities specified in subparagraphs (A) and (B).",
      "versionDate": "2026-02-25",
      "versionType": "Introduced in House"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-03-16T16:34:45Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7696ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "AI Cyber Grid Protection Resilient Development Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-14T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AI Cyber Grid Protection Resilient Development Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-14T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program to provide awards to National Laboratories and institutions of higher education to develop secure artificial intelligence (AI) cyber-physical testbeds to simulate grid-scale cyberattacks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-14T03:48:24Z"
    }
  ]
}
```
