# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/355?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/355
- Title: FDA Modernization Act 3.0
- Congress: 119
- Bill type: S
- Bill number: 355
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2026-03-12T15:10:11Z
- Update date including text: 2026-03-12T15:10:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-12-16 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S8793-8794)
- 2025-12-16 - Floor: Passed Senate with an amendment by Unanimous Consent. (text of amendment in the nature of a substitute: CR S8794)
- 2025-12-16 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-12-16 - Discharge: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- 2025-12-16 - Committee: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- 2025-12-17 - Floor: Message on Senate action sent to the House.
- 2025-12-17 09:58:54 - Floor: Received in the House.
- 2025-12-17 10:21:29 - Floor: Held at the desk.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-12-16 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S8793-8794)
- 2025-12-16 - Floor: Passed Senate with an amendment by Unanimous Consent. (text of amendment in the nature of a substitute: CR S8794)
- 2025-12-16 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-12-16 - Discharge: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- 2025-12-16 - Committee: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- 2025-12-17 - Floor: Message on Senate action sent to the House.
- 2025-12-17 09:58:54 - Floor: Received in the House.
- 2025-12-17 10:21:29 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/355",
    "number": "355",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "FDA Modernization Act 3.0",
    "type": "S",
    "updateDate": "2026-03-12T15:10:11Z",
    "updateDateIncludingText": "2026-03-12T15:10:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-17",
      "actionTime": "10:21:29",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-17",
      "actionTime": "09:58:54",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (text of amendment in the nature of a substitute: CR S8794)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S8793-8794)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-12-16",
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
      "text": "Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-03",
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
      "actionDate": "2025-02-03",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2025-12-16",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 4057 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2025-12-16",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 4057 proposed by Senator Thune for Senator Booker. (consideration: CR S8794) In the nature of a substitute.",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-12-16",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2025-12-16",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 4057 proposed by Senator Thune for Senator Booker.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-12-16",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2025-12-16",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 4057 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "355",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "FDA Modernization Act 3.0",
          "type": "S",
          "updateDateIncludingText": "2026-03-12"
        },
        "chamber": "Senate",
        "congress": "119",
        "cosponsors": {
          "count": "1",
          "countIncludingWithdrawnCosponsors": "1",
          "item": {
            "bioguideId": "S001227",
            "firstName": "Eric",
            "fullName": "Sen. Schmitt, Eric [R-MO]",
            "isOriginalCosponsor": "True",
            "lastName": "Schmitt",
            "middleName": "S.",
            "party": "R",
            "sponsorshipDate": "2025-12-16",
            "state": "MO"
          }
        },
        "latestAction": {
          "actionDate": "2025-12-16",
          "links": {
            "link": {
              "name": "SA 4057",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/4057"
            }
          },
          "text": "Amendment SA 4057 agreed to in Senate by Unanimous Consent."
        },
        "number": "4057",
        "onBehalfOfSponsor": {
          "item": [
            {
              "bioguideId": "T000250",
              "firstName": "John",
              "fullName": "Sen. Thune, John [R-SD]",
              "lastName": "Thune",
              "party": "R",
              "state": "SD",
              "type": "Submitted on behalf of"
            },
            {
              "bioguideId": "T000250",
              "firstName": "John",
              "fullName": "Sen. Thune, John [R-SD]",
              "lastName": "Thune",
              "party": "R",
              "state": "SD",
              "type": "Proposed on behalf of"
            }
          ]
        },
        "proposedDate": "2025-12-17T00:52:54Z",
        "purpose": "In the nature of a substitute.",
        "sponsors": {
          "item": {
            "bioguideId": "B001288",
            "firstName": "Cory",
            "fullName": "Sen. Booker, Cory A. [D-NJ]",
            "lastName": "Booker",
            "party": "D",
            "state": "NJ"
          }
        },
        "submittedDate": "2025-12-16T05:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2025-12-17T01:03:27Z"
      }
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
            "date": "2025-12-17T00:52:52Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-02-03T20:55:42Z",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "MO"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-03",
      "state": "ME"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "RI"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "KS"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "CT"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "KY"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s355is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 355\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mr. Booker (for himself, Mr. Schmitt , Mr. King , Mr. Kennedy , Mr. Whitehouse , Mr. Marshall , Mr. Blumenthal , Mr. Paul , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to publish a final rule relating to nonclinical testing methods.\n#### 1. Short title\nThis Act may be cited as the FDA Modernization Act 3.0 .\n#### 2. Regulations on nonclinical testing methods\n##### (a) Interim final rule\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall publish an interim final rule pursuant to subsections (b) and (c) to ensure implementation of the amendments to section 505(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(i) ) made by section 3209(a) of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 ; 136 Stat. 5821).\n**(2) Effectiveness of interim final rule**\nNotwithstanding subparagraph (B) of section 553(b) of title 5, United States Code, the interim final rule issued by the Secretary of Health and Human Services under paragraph (1) shall become immediately effective as an interim final rule without requiring the Secretary of Health and Human Services to demonstrate good cause therefor.\n##### (b) Inclusions\n**(1) In general**\nThe interim final rule shall replace any references to animal tests, data, studies, models, and research with a reference to nonclinical tests, data, studies, models, and research in the following sections of title 21, Code of Federal Regulations:\n**(A)**\nSection 312.22(c).\n**(B)**\nSection 312.23(a)(3)(iv).\n**(C)**\nSection 312.23(a)(5)(ii).\n**(D)**\nSection 312.23(a)(5)(iii).\n**(E)**\nSection 312.23(a)(8).\n**(F)**\nSection 312.23(a)(8)(i).\n**(G)**\nSection 312.23(a)(8)(ii).\n**(H)**\nSection 312.23(a)(10)(i).\n**(I)**\nSection 312.23(a)(10)(ii).\n**(J)**\nSection 312.33(b)(6).\n**(K)**\nSection 312.82(a).\n**(L)**\nSection 312.88.\n**(M)**\nSection 314.50(d)(2).\n**(N)**\nSection 314.50(d)(2)(iv).\n**(O)**\nSection 314.50(d)(5)(i).\n**(P)**\nSection 314.50(d)(5)(vi)(a).\n**(Q)**\nSection 314.50(d)(5)(vi)(b).\n**(R)**\nSection 314.93(e)(2).\n**(S)**\nSection 315.6(d).\n**(T)**\nSection 330.10(a)(2).\n**(U)**\nSection 601.35(d).\n**(V)**\nAny other section necessary to ensure regulatory consistency with the amendments to section 505(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(i) ) made by section 3209(a) of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 ; 136 Stat. 5821).\n**(2) Additional changes**\nThe Secretary may make such additional changes to the sections of title 21, Code of Federal Regulations, described in subparagraphs (A) through (V) of paragraph (1) as the Secretary determines appropriate to fully implement the replacement required under such paragraph.\n##### (c) Definition of nonclinical test\nThe definition of nonclinical test in section 505(z) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(z) ) shall be added to sections 312.3, 314.3, 315.2, and 601.31 of title 21, Code of Federal Regulations.\n##### (d) Technical amendment\nSection 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) is amended by designating the second subsection (z) (relating to clinical trial diversity action plans), as added by section 3601(a) of the Health Extenders, Improving Access to Medicare, Medicaid, and CHIP, and Strengthening Public Health Act of 2022 (division FF of Public Law 117\u2013328 ), as subsection (aa).",
      "versionDate": "2025-02-03",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s355es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 355\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo require the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to publish a final rule relating to nonclinical testing methods.\n#### 1. Short title\nThis Act may be cited as the FDA Modernization Act 3.0 .\n#### 2. Regulations on nonclinical testing methods\n##### (a) Interim final rule\n**(1) In general**\nIn order to ensure implementation of the amendments to section 505(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(i) ) made by section 3209(a) of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 ; 136 Stat. 5821), not later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall publish an interim final rule\u2014\n**(A)**\nto amend the sections of title 21, Code of Federal Regulations, described in paragraph (2) to replace any references to animal tests, data, studies, models, and research with a reference to nonclinical tests, data, studies, models, and research; and\n**(B)**\nto add the definition of nonclinical test in section 505(z) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(z) ) to sections 312.3, 314.3, 315.2, and 601.31 of title 21, Code of Federal Regulations.\n**(2) CFR sections described**\nThe sections of title 21, Code of Federal Regulations, described in this paragraph are the following:\n**(A)**\nSection 312.22(c).\n**(B)**\nSection 312.23(a)(3)(iv).\n**(C)**\nSection 312.23(a)(5)(ii).\n**(D)**\nSection 312.23(a)(5)(iii).\n**(E)**\nSection 312.23(a)(8).\n**(F)**\nSection 312.23(a)(8)(i).\n**(G)**\nSection 312.23(a)(8)(ii).\n**(H)**\nSection 312.23(a)(10)(i).\n**(I)**\nSection 312.23(a)(10)(ii).\n**(J)**\nSection 312.33(b)(6).\n**(K)**\nSection 312.82(a).\n**(L)**\nSection 312.88.\n**(M)**\nSection 314.50(d)(2).\n**(N)**\nSection 314.50(d)(2)(iv).\n**(O)**\nSection 314.50(d)(5)(i).\n**(P)**\nSection 314.50(d)(5)(vi)(a).\n**(Q)**\nSection 314.50(d)(5)(vi)(b).\n**(R)**\nSection 314.93(e)(2).\n**(S)**\nSection 315.6(d).\n**(T)**\nSection 330.10(a)(2).\n**(U)**\nSection 601.35(d).\n**(V)**\nAny other section necessary to ensure regulatory consistency with the amendments to section 505(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(i) ) made by section 3209(a) of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 ; 136 Stat. 5821).\n**(3) Effectiveness of interim final rule**\nNotwithstanding subparagraph (B) of section 553(b) of title 5, United States Code, the interim final rule issued by the Secretary of Health and Human Services under paragraph (1) shall become immediately effective as an interim final rule without requiring the Secretary of Health and Human Services to demonstrate good cause therefor.\n##### (b) Technical amendment\nSection 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) is amended by designating the second subsection (z) (relating to clinical trial diversity action plans), as added by section 3601(a) of the Health Extenders, Improving Access to Medicare, Medicaid, and CHIP, and Strengthening Public Health Act of 2022 (division FF of Public Law 117\u2013328 ), as subsection (aa).",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-04-07T15:23:32Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-04-07T15:23:32Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-04-07T15:23:32Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-04-07T15:23:32Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-04-07T15:23:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-10T14:11:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-03",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s355",
          "measure-number": "355",
          "measure-type": "s",
          "orig-publish-date": "2025-02-03",
          "originChamber": "SENATE",
          "update-date": "2025-06-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s355v00",
            "update-date": "2025-06-04"
          },
          "action-date": "2025-02-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>FDA Modernization Act 3.0</strong></p><p>This bill requires the Food and Drug Administration (FDA) to publish an interim final rule implementing a provision of the Consolidated Appropriations Act of 2023 that authorized the use of certain alternatives to animal testing to support investigational use of a new drug.\u00a0</p><p>The rule must replace references to animal tests, data, studies, models, and research with references to nonclinical tests, data, studies, models, and research throughout the FDA\u2019s regulations governing investigational new drug applications, and may make other changes to the regulations as appropriate.\u00a0</p><p>The rule must be published within one year of the bill\u2019s enactment, and must take immediate effect as an interim final rule.\u00a0</p>"
        },
        "title": "FDA Modernization Act 3.0"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s355.xml",
    "summary": {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>FDA Modernization Act 3.0</strong></p><p>This bill requires the Food and Drug Administration (FDA) to publish an interim final rule implementing a provision of the Consolidated Appropriations Act of 2023 that authorized the use of certain alternatives to animal testing to support investigational use of a new drug.\u00a0</p><p>The rule must replace references to animal tests, data, studies, models, and research with references to nonclinical tests, data, studies, models, and research throughout the FDA\u2019s regulations governing investigational new drug applications, and may make other changes to the regulations as appropriate.\u00a0</p><p>The rule must be published within one year of the bill\u2019s enactment, and must take immediate effect as an interim final rule.\u00a0</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119s355"
    },
    "title": "FDA Modernization Act 3.0"
  },
  "summaries": [
    {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>FDA Modernization Act 3.0</strong></p><p>This bill requires the Food and Drug Administration (FDA) to publish an interim final rule implementing a provision of the Consolidated Appropriations Act of 2023 that authorized the use of certain alternatives to animal testing to support investigational use of a new drug.\u00a0</p><p>The rule must replace references to animal tests, data, studies, models, and research with references to nonclinical tests, data, studies, models, and research throughout the FDA\u2019s regulations governing investigational new drug applications, and may make other changes to the regulations as appropriate.\u00a0</p><p>The rule must be published within one year of the bill\u2019s enactment, and must take immediate effect as an interim final rule.\u00a0</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119s355"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s355is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s355es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "FDA Modernization Act 3.0",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "FDA Modernization Act 3.0",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-17T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FDA Modernization Act 3.0",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to publish a final rule relating to nonclinical testing methods.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T02:48:26Z"
    }
  ]
}
```
