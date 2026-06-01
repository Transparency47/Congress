# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5007?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5007
- Title: To direct the Director of the U.S. Immigration and Customs Enforcement to report on information about arrests made by U.S. Immigration and Customs Enforcement.
- Congress: 119
- Bill type: HR
- Bill number: 5007
- Origin chamber: House
- Introduced date: 2025-08-19
- Update date: 2026-02-06T09:06:34Z
- Update date including text: 2026-02-06T09:06:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-19: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-19: Introduced in House

## Actions

- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-19",
    "latestAction": {
      "actionDate": "2025-08-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5007",
    "number": "5007",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "To direct the Director of the U.S. Immigration and Customs Enforcement to report on information about arrests made by U.S. Immigration and Customs Enforcement.",
    "type": "HR",
    "updateDate": "2026-02-06T09:06:34Z",
    "updateDateIncludingText": "2026-02-06T09:06:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-19",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-08-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-19",
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
          "date": "2025-08-19T14:01:20Z",
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
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "VA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5007ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5007\nIN THE HOUSE OF REPRESENTATIVES\nAugust 19, 2025 Mr. Subramanyam (for himself and Ms. McClellan ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Director of the U.S. Immigration and Customs Enforcement to report on information about arrests made by U.S. Immigration and Customs Enforcement.\n#### 1. Report on information about arrests made by U.S. Immigration and Customs Enforcement\n##### (a) In general\nNot later than 30 days after the date of the enactment of this Act, and quarterly thereafter, the Director of the U.S. Immigration and Customs Enforcement shall report the following:\n**(1)**\nThe total number of arrests made in the immediately previous quarter.\n**(2)**\nThe total number of detainees in the custody of the Secretary of Homeland Security during immediately previous quarter.\n**(3)**\nThe total number of individuals deported from the United States in the immediately previous quarter.\n**(4)**\nFor paragraph (1) through (3), the following:\n**(A)**\nThe percentage of individuals who were convicted of a criminal offense under State or Federal law.\n**(B)**\nThe percentage of individuals designated as\u2014\n**(i)**\nA ICE Threat Level 1 Offender.\n**(ii)**\nA ICE Threat Level 2 Offender.\n**(iii)**\nA ICE Threat Level 3 Offender.\n**(iv)**\nAn alien that is not designated under clauses (i) through (iii).\n##### (b) Publication\nThe report under subsection (a) shall be published on the internet website of the U.S. Immigration and Customs Enforcement.\n##### (c) Definitions\nIn this section:\n**(1) ICE Threat Level 1 Offender**\nThe term ICE Threat Level 1 Offender means an alien\u2014\n**(A)**\nconvicted of an aggravated felony (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )); or\n**(B)**\nconvicted of two or more offenses under State or Federal law that are punishable by a term of imprisonment of more than one year.\n**(2) ICE Threat Level 2 Offender**\nThe term ICE Threat Level 2 Offender means an alien\u2014\n**(A)**\nconvicted of an offense under State or Federal law that is punishable by a term of imprisonment of more than one year; or\n**(B)**\nconvicted of three or more offenses under State or Federal law that are punishable by a term of imprisonment of less than one year.\n**(3) ICE Threat Level 3 Offender**\nThe term ICE Threat Level 2 Offender means an alien convicted of an offense under State or Federal law that is punishable by a term of imprisonment of less than one year.",
      "versionDate": "2025-08-19",
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
        "name": "Immigration",
        "updateDate": "2025-09-19T14:24:26Z"
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
      "date": "2025-08-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5007ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of the U.S. Immigration and Customs Enforcement to report on information about arrests made by U.S. Immigration and Customs Enforcement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-20T09:12:00Z"
    },
    {
      "title": "To direct the Director of the U.S. Immigration and Customs Enforcement to report on information about arrests made by U.S. Immigration and Customs Enforcement.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-20T08:05:29Z"
    }
  ]
}
```
