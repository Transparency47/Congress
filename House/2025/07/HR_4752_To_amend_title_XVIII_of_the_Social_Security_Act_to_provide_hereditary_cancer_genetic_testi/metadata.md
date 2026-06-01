# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4752?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4752
- Title: Reducing Hereditary Cancer Act
- Congress: 119
- Bill type: HR
- Bill number: 4752
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-13T08:06:41Z
- Update date including text: 2026-05-13T08:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4752",
    "number": "4752",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000797",
        "district": "25",
        "firstName": "Debbie",
        "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
        "lastName": "Wasserman Schultz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Reducing Hereditary Cancer Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:41Z",
    "updateDateIncludingText": "2026-05-13T08:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:12:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:12:10Z",
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "IA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "TN"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "MI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NJ"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "IN"
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
      "sponsorshipDate": "2025-08-15",
      "state": "DC"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "OR"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "IA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "DE"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-13",
      "state": "NE"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "PA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CT"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "VA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "UT"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MI"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "IL"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "AL"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "AZ"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4752ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4752\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Wasserman Schultz (for herself, Mrs. Miller-Meeks , Ms. Schrier , and Mr. Buchanan ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide hereditary cancer genetic testing for individuals with a history of a hereditary cancer gene mutation in a blood relative or a personal or ancestral history suspicious for hereditary cancer, and to provide coverage of certain cancer screenings or preventive surgeries that would reduce the risk for individuals with a germline (inherited) mutation associated with a high risk of developing a preventable cancer.\n#### 1. Short title\nThis Act may be cited as the Reducing Hereditary Cancer Act .\n#### 2. Hereditary cancer genetic testing of individuals with a family history of a hereditary cancer gene mutation or personal or family history suspicious for hereditary cancer\n##### (a) Coverage\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (s)(2)\u2014\n**(A)**\nby striking and at the end of subparagraph (II);\n**(B)**\nby striking the period and inserting ; and at the end of subparagraph (JJ); and\n**(C)**\nby inserting after subparagraph (JJ) the following new subparagraph:\n(KK) in the case of an individual with a personal or family history of a hereditary cancer gene mutation or a personal or family history suspicious for hereditary cancer, germline mutation testing. ; and\n**(2)**\nby adding at the end the following new subsection:\n(nnn) Germline mutation testing The term germline mutation testing means genetic testing for germline mutations that is in accordance with evidence-based, clinical practice guidelines specifically addressing genetic testing, screening, and management of individuals with inherited mutations associated with increased cancer risk that\u2014 (1) have been developed by a nationally recognized oncology professional organization, including the National Comprehensive Cancer Network, the American Society of Clinical Oncology, the Society of Gynecologic Oncology, or any other oncology professional organization specified by a medicare administrative contractor with a contract under section 1874A; and (2) in the case of conflicting guidelines developed by more than one nationally recognized oncology professional organization, the least restrictive of such guidelines, as determined by such a medicare administrative contractor. .\n##### (b) Frequency\nSection 1862(a)(1) of the Social Security Act ( 42 U.S.C. 1395y(a)(1) ) is amended\u2014\n**(1)**\nby striking and at the end of subparagraph (O);\n**(2)**\nby adding and at the end of subparagraph (P); and\n**(3)**\nby adding at the end the following new subparagraph:\n(Q) in the case of germline mutation testing as defined in section 1861(lll), which is performed more than once with respect to an individual described in such section; .\n##### (c) Effective date\nThe amendments made by this section shall apply to testing furnished on or after the date of the enactment of this Act.\n#### 3. Coverage of certain preventive surgeries\n##### (a) In general\nSection 1862 of the Social Security Act ( 42 U.S.C. 1395y ) is amended by adding at the end the following new subsection:\n(p) Coverage of certain risk-Reducing surgeries In the case of an individual described in section 1861(s)(2)(II) for whom, based on evidence-based, clinical practice guidelines described in section 1861(lll), surgery would reduce the risk of developing cancer, such risk-reducing surgery shall be considered reasonable and necessary for treatment of illness under subsection (a)(1)(A). .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply to items and services furnished on or after the date of the enactment of this Act.\n#### 4. Coverage of evidence-based screenings for individuals with a hereditary cancer gene mutation\n##### (a) In general\nSection 1862 of the Social Security Act ( 42 U.S.C. 1395y ), as amended by section 3, is amended by adding at the end the following new subsection:\n(q) Coverage of evidence-Based screenings for individuals with a hereditary cancer gene mutation In the case of an individual who is determined pursuant to genetic testing to have a hereditary cancer (germline) gene mutation, the Secretary shall increase any frequency limitations (or other limitations on coverage otherwise applicable under this title) for any evidence-based screenings furnished to such individual, to be in compliance with evidence-based, clinical practice guidelines described in section 1861(lll), or as determined appropriate by the Secretary, but not less frequently than on an annual basis. For the purposes of this subsection, evidence-based screenings shall include screening mammography, breast screening MRI, colonoscopy, PSA testing, and any additional evidence-based screening modalities appropriate for high-risk individuals as recommended by such guidelines. .\n##### (b) Conforming amendment for screening mammography\nSection 1834(c)(2)(A) of the Social Security Act ( 42 U.S.C. 1395m(c)(2)(A) ) is amended, in the matter preceding clause (i), by striking subparagraph (B) and inserting subparagraph (B) and section 1862(q) .\n##### (c) Effective date\nThe amendments made by this section shall apply to items and services furnished on or after the date of the enactment of this Act.",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-09-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2760",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Reducing Hereditary Cancer Act of 2025",
      "type": "S"
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
        "updateDate": "2025-09-16T17:32:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
    "originChamber": "House",
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
          "measure-id": "id119hr4752",
          "measure-number": "4752",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4752v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Reducing Hereditary Cancer Act</b></p> <p>This bill provides for Medicare coverage of germline mutation testing for individuals with a personal or family history of a hereditary cancer gene mutation or suspected history of hereditary cancer, as well as for associated coverage of risk-reducing surgeries and screenings.</p>"
        },
        "title": "Reducing Hereditary Cancer Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4752.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Reducing Hereditary Cancer Act</b></p> <p>This bill provides for Medicare coverage of germline mutation testing for individuals with a personal or family history of a hereditary cancer gene mutation or suspected history of hereditary cancer, as well as for associated coverage of risk-reducing surgeries and screenings.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4752"
    },
    "title": "Reducing Hereditary Cancer Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Reducing Hereditary Cancer Act</b></p> <p>This bill provides for Medicare coverage of germline mutation testing for individuals with a personal or family history of a hereditary cancer gene mutation or suspected history of hereditary cancer, as well as for associated coverage of risk-reducing surgeries and screenings.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4752"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4752ih.xml"
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
      "title": "Reducing Hereditary Cancer Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reducing Hereditary Cancer Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide hereditary cancer genetic testing for individuals with a history of a hereditary cancer gene mutation in a blood relative or a personal or ancestral history suspicious for hereditary cancer, and to provide coverage of certain cancer screenings or preventive surgeries that would reduce the risk for individuals with a germline (inherited) mutation associated with a high risk of developing a preventable cancer.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:36Z"
    }
  ]
}
```
