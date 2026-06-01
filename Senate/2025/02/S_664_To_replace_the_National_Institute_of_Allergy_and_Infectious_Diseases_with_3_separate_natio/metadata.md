# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/664?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/664
- Title: NIH Reform Act
- Congress: 119
- Bill type: S
- Bill number: 664
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-12-05T22:48:26Z
- Update date including text: 2025-12-05T22:48:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/664",
    "number": "664",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "NIH Reform Act",
    "type": "S",
    "updateDate": "2025-12-05T22:48:26Z",
    "updateDateIncludingText": "2025-12-05T22:48:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-20T18:27:05Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s664is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 664\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Paul (for himself and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo replace the National Institute of Allergy and Infectious Diseases with 3 separate national research institutes.\n#### 1. Short title\nThis Act may be cited as the NIH Reform Act .\n#### 2. Division of National Institute of Allergy and Infectious Diseases\n##### (a) Organization of national research institutes\nSection 401 of the Public Health Service Act ( 42 U.S.C. 281 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (6), by striking Allergy and Infectious Diseases and inserting Allergic Diseases ;\n**(B)**\nby redesignating paragraph (25) as paragraph (27); and\n**(C)**\nby inserting after paragraph (24) the following:\n(25) The National Institute of Infectious Diseases. (26) The National Institute of Immunologic Diseases. ; and\n**(2)**\nin subsection (d)(1), by striking 27 and inserting 29 .\n##### (b) Appointment of directors\n**(1) In general**\nSection 405(a)(1) of the Public Health Service Act ( 42 U.S.C. 284(a)(1) ) is amended\u2014\n**(A)**\nby inserting , the Director of the National Institute of Allergic Diseases, the Director of the National Institute of Infectious Diseases, and the Director of the National Institute of Immunologic Diseases after National Cancer Institute ; and\n**(B)**\nby inserting by and with the advice and consent of the Senate, after the President, .\n**(2) Terms**\nSection 405(a) of the Public Health Service Act ( 42 U.S.C. 284(a) ) is amended by adding at the end the following:\n(4) Certain appointments by the President The appointments by the President of the Director of the National Institute of Allergic Diseases, the Director of the National Institute of Infectious Diseases, and the Director of the National Institute of Immunologic Diseases shall be for terms of 5 years. Each such Director may be reappointed for not more than 1 additional term, in accordance paragraph (1). .\n**(3) Transition**\nEffective on the date of enactment of this Act, the position of Director of the National Institute of Allergy and Infectious Diseases is terminated, and the National Institute of Allergic Diseases, the National Institute of Infectious Diseases, and the National Institute of Immunologic Diseases shall be overseen by the Director of the National Institutes of Health until such time as the directors of each such national institutes is appointed pursuant to section 405(a)(1) of the Public Health Service Act ( 42 U.S.C. 284(a)(1) ), as amended by paragraph (1).\n##### (c) Duties of the National Institutes\n**(1) National Institute of Allergic Diseases**\nSubpart 6 of part C of title IV of the Public Health Service Act ( 42 U.S.C. 285f et seq. ) is amended\u2014\n**(A)**\nin the subpart heading, by striking Allergy and infectious diseases and inserting Allergic Diseases ; and\n**(B)**\nin section 446\u2014\n**(i)**\nby striking Allergy and Infectious Diseases and inserting Allergic Diseases ; and\n**(ii)**\nby striking allergic and immunologic diseases and disorders and infectious diseases, including tropical diseases and inserting allergic diseases and disorders .\n**(2) National Institute of Infectious Diseases**\n**(A) In general**\nPart C of title IV of the Public Health Service Act ( 42 U.S.C. 285 et seq. ) is amended by adding at the end the following:\n21 National Institute of Infectious Diseases 464z\u201310. Purpose of the Institute The general purpose of the National Institute of Infectious Diseases is the conduct and support of research, training, health information dissemination, and other programs with respect to infectious diseases, including tropical diseases. .\n**(B) Transfer of authorities**\nSections 447A and 447B of the Public Health Service Act ( 42 U.S.C. 285f\u20132 ; 285f\u20133) are\u2014\n**(i)**\nredesignated as sections 464z\u201311 and 464z\u201312, respectively; and\n**(ii)**\ntransferred to appear after section 464z\u201310 of such Act, as added by subparagraph (A).\n**(C) Orderly transition**\nThe Director of the National Institutes of Health shall take such steps as are necessary to provide for the orderly transition to the authority of the National Institute of Infectious Diseases established under section 464z\u201310 of the Public Health Service Act, as added by subparagraph (A), from any authority related to infectious diseases of the National Institute of Allergy and Infectious Diseases, as in effect on the day before the date of enactment of this Act.\n**(3) National Institute of Immunologic Diseases**\n**(A) In general**\nPart C of title IV of the Public Health Service Act ( 42 U.S.C. 285 et seq. ), as amended by paragraph (2), is further amended by adding at the end the following:\n22 National Institute of Immunologic Diseases 464z\u201315. Purpose of the Institute The general purpose of the National Institute of Immunologic Diseases is the conduct and support of research, training, health information dissemination, and other programs with respect to immunologic diseases and disorders. .\n**(B) Transfer of authorities**\nSections 447 and 447C of the Public Health Service Act ( 42 U.S.C. 285f\u20131 ; 285f\u20134) are\u2014\n**(i)**\nredesignated as sections 464z\u201316 and 464z\u201317, respectively; and\n**(ii)**\ntransferred to appear after section 464z\u201315 of such Act, as added by subparagraph (A).\n**(C) Orderly transition**\nThe Director of the National Institutes of Health shall take such steps as are necessary to provide for the orderly transition to the authority of the National Institute of Immunologic Diseases established under section 464z\u201315 of the Public Health Service Act, as added by subparagraph (A), from any authority related to immunologic diseases and disorders of the National Institute of Allergy and Infectious Diseases, as in effect on the day before the date of enactment of this Act.\n##### (d) Conforming amendments\n**(1)**\nSection 404B of the Public Health Service Act ( 42 U.S.C. 283d ) is amended by striking National Institute for Allergy and Infectious Diseases and inserting National Institute for Infectious Diseases .\n**(2)**\nSection 404I of the Public Health Service Act ( 42 U.S.C. 283k ) is amended\u2014\n**(A)**\nin subsection (a)(1), by striking or the Director of the National Institute for Allergy and Infectious Diseases ; and\n**(B**\nby striking or the National Institute for Allergy and Infectious Diseases each place it appears.\n**(3)**\nSection 442A(a) of the Public Health Service Act ( 42 U.S.C. 285d\u20138(a) ) is amended by striking Allergy and Infectious Diseases and inserting Immunologic Diseases .\n##### (e) References in law\nAny reference in any law (including a regulation), guidance, map, document, record, or other paper of the United States to the National Institute of Allergy and Infectious Diseases, including with respect to the Director of such Institute, shall be deemed to be a reference to, as applicable, the National Institute of Allergic Diseases, the National Institute of Infectious Diseases, or the National Institute of Immunologic Diseases, including with respect to the Directors of such Institutes.",
      "versionDate": "2025-02-20",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-21",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1497",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NIH Reform Act",
      "type": "HR"
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
            "name": "Allergies",
            "updateDate": "2025-07-10T16:16:57Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-07-10T16:16:57Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-07-10T16:16:57Z"
          },
          {
            "name": "Immunology and vaccination",
            "updateDate": "2025-07-10T16:16:57Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-07-10T16:16:57Z"
          },
          {
            "name": "National Institutes of Health (NIH)",
            "updateDate": "2025-07-10T16:16:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-13T17:22:28Z"
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
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s664is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "NIH Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NIH Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to replace the National Institute of Allergy and Infectious Diseases with 3 separate national research institutes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:43Z"
    }
  ]
}
```
