# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/158?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/158
- Title: A resolution expressing the sense of the Senate that paraprofessionals and education support staff should have fair compensation, benefits, and working conditions.
- Congress: 119
- Bill type: SRES
- Bill number: 158
- Origin chamber: Senate
- Introduced date: 2025-04-07
- Update date: 2026-02-25T12:22:48Z
- Update date including text: 2026-02-25T12:22:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in Senate
- 2025-04-07 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2457-2458)
- 2025-04-07 - IntroReferral: Submitted in Senate
- Latest action: 2025-04-07: Submitted in Senate

## Actions

- 2025-04-07 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2457-2458)
- 2025-04-07 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/158",
    "number": "158",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A resolution expressing the sense of the Senate that paraprofessionals and education support staff should have fair compensation, benefits, and working conditions.",
    "type": "SRES",
    "updateDate": "2026-02-25T12:22:48Z",
    "updateDateIncludingText": "2026-02-25T12:22:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2457-2458)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
        "item": [
          {
            "date": "2025-04-07T19:38:37Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-07T19:38:37Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-04-07",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NM"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NM"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "DE"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres158is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 158\nIN THE SENATE OF THE UNITED STATES\nApril 7, 2025 Mr. Markey (for himself, Mr. Sanders , Mr. Merkley , Mr. Padilla , Mr. Booker , Mr. Heinrich , and Ms. Warren ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing the sense of the Senate that paraprofessionals and education support staff should have fair compensation, benefits, and working conditions.\nThat it is the sense of the Senate that\u2014\n**(1)**\nparaprofessionals and education support staff\u2014\n**(A)**\nshould be compensated at a rate that is a livable, competitive wage;\n**(B)**\nshould have access to high-quality, affordable healthcare and healthcare benefits at a de minimus personal cost;\n**(C)**\nshould be considered to be eligible employees under the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2601 et seq. );\n**(D)**\nshould be entitled to 16 weeks of paid family and medical leave;\n**(E)**\nshould have paid leave for all planned and unforeseen school closures, including weather-related closures, professional development days, and other short-term closures;\n**(F)**\nshould have access to meaningful and free or affordable professional growth and development opportunities during regular paid working hours that provide a path to career advancement;\n**(G)**\nshould have sufficient resources and supplies to enable them to do their job effectively and efficiently, including up-to-date technology;\n**(H)**\nshould have access to training and appropriate personal protective equipment;\n**(I)**\nshould have representation in organizations that determine policies that may affect the working conditions of paraprofessionals and education support staff;\n**(J)**\nshould receive notification and the opportunity to provide significant input about the implementation of electronic monitoring, data, algorithms, and artificial intelligence technology in the applicable school and should receive high-quality professional development as new technologies are introduced;\n**(K)**\nshould have adequate notice and opportunity to participate, when appropriate, in individualized education program meetings, behavior intervention team meetings, and other similar meetings relating to the students the paraprofessionals and education support staff support, to the extent permitted by law;\n**(L)**\nshould experience a safe and healthy working environment free from recognized hazards that cause or are likely to cause death or serious physical harm;\n**(M)**\nshould experience appropriate staffing levels to ensure that students have adequate support and that paraprofessionals and education support staff can complete their jobs effectively, efficiently, and safely;\n**(N)**\nshould receive adequate notification regarding the duration of their employment;\n**(O)**\nshould have an employment contract that includes a provision for the automatic renewal of the contract at the expiration of the contract, rather than the automatic termination of the contract at such expiration, and a provision for termination of employment for just cause, rather than termination of employment at will; and\n**(P)**\nshould have a process for reporting workplace issues and concerns to their employer in a manner that protects paraprofessionals and education support staff and other employees from retaliation;\n**(2)**\nin recognition of the importance of collective bargaining in maintaining good working conditions, employers of paraprofessionals and education support staff should\u2014\n**(A)**\nengage in good faith negotiations;\n**(B)**\nstrive to reach timely and just contracts that fairly compensate and protect paraprofessionals and education support staff;\n**(C)**\nrefrain from replacing paraprofessionals or education support staff who engage in a strike; and\n**(D)**\nrefrain from locking out such workers; and\n**(3)**\nnothing in this resolving clause should be interpreted to supersede, or as an expression of the Senate's support for any law that would supersede, employment terms or conditions agreed upon in collective bargaining agreements that are more beneficial to paraprofessionals and education support staff than those described in this resolving clause.",
      "versionDate": "2025-04-07",
      "versionType": "IS"
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
        "actionDate": "2025-04-07",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "297",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing the sense of the House of Representatives that paraprofessionals and education support staff should have fair compensation, benefits, and working conditions.",
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
        "name": "Education",
        "updateDate": "2025-04-10T12:55:17Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres158is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing the sense of the Senate that paraprofessionals and education support staff should have fair compensation, benefits, and working conditions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:32Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate that paraprofessionals and education support staff should have fair compensation, benefits, and working conditions.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T10:56:17Z"
    }
  ]
}
```
