# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/932?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/932
- Title: Give Kids a Chance Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 932
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-02-05T17:34:07Z
- Update date including text: 2026-02-05T17:34:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/932",
    "number": "932",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001190",
        "district": "",
        "firstName": "Markwayne",
        "fullName": "Sen. Mullin, Markwayne [R-OK]",
        "lastName": "Mullin",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Give Kids a Chance Act of 2025",
    "type": "S",
    "updateDate": "2026-02-05T17:34:07Z",
    "updateDateIncludingText": "2026-02-05T17:34:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T17:00:22Z",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CO"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "NH"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "KS"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "FL"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ME"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "DE"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "WV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "AZ"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "OH"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "NJ"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "MT"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "FL"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "CO"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "IL"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "AR"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "LA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "RI"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s932is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 932\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Mullin (for himself and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act with respect to molecularly targeted pediatric cancer investigations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Give Kids a Chance Act of 2025 .\n#### 2. Research into pediatric uses of drugs; additional authorities of Food and Drug Administration regarding molecularly targeted cancer drugs\n##### (a) In general\n**(1) Additional active ingredient for application drug; limitation regarding novel-combination application drug**\nSection 505B(a)(3) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355c(a)(3) ) is amended\u2014\n**(A)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (C) and (D), respectively; and\n**(B)**\nby striking subparagraph (A) and inserting the following:\n(A) In general For purposes of paragraph (1)(B), the investigation described in this paragraph is a molecularly targeted pediatric cancer investigation of\u2014 (i) the drug or biological product for which the application referred to in such paragraph is submitted; or (ii) such drug or biological product used in combination with\u2014 (I) an active ingredient of a drug or biological product\u2014 (aa) for which an approved application under section 505(j) under this Act or under section 351(k) of the Public Health Service Act is in effect; and (bb) that is determined by the Secretary, after consultation with the applicant, to be part of the standard of care for treating a pediatric cancer; or (II) an active ingredient of a drug or biological product\u2014 (aa) for which an approved application under section 505(b) of this Act or section 351(a) of the Public Health Service Act to treat an adult cancer is in effect and is held by the same person submitting the application under paragraph (1)(B); and (bb) that is directed at a molecular target that the Secretary determines to be substantially relevant to the growth or progression of a pediatric cancer. (B) Additional requirements (i) Design of investigation A molecularly targeted pediatric cancer investigation referred to in subparagraph (A) shall be designed to yield clinically meaningful pediatric study data that is gathered using appropriate formulations for each age group for which the study is required, regarding dosing, safety, and preliminary efficacy to inform potential pediatric labeling. (ii) Limitation An investigation described in subparagraph (A)(ii) may be required only if the drug or biological product for which the application referred to in paragraph (1)(B) contains either\u2014 (I) a single new active ingredient; or (II) more than one active ingredient, if an application for the combination of active ingredients has not previously been approved but each active ingredient is in a drug product that has been previously approved to treat an adult cancer. (iii) Results of already-completed preclinical studies of application drug With respect to an investigation required pursuant to paragraph (1)(B), the Secretary may require the results of any completed preclinical studies relevant to the initial pediatric study plan be submitted to the Secretary at the same time that the initial pediatric study plan required under subsection (e)(1) is submitted. (iv) Rule of construction regarding inactive ingredients With respect to a combination of active ingredients referred to in subparagraph (A)(ii), such subparagraph shall not be construed as addressing the use of inactive ingredients with such combination. .\n**(2) Determination of applicable requirements**\nSection 505B(e)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355c(e)(1) ) is amended by adding at the end the following: The Secretary shall determine whether subparagraph (A) or (B) of subsection (a)(1) applies with respect to an application before the date on which the applicant is required to submit the initial pediatric study plan under paragraph (2)(A). .\n**(3) Clarifying applicability**\nSection 505B(a)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355c(a)(1) ) is amended by adding at the end the following:\n(C) Rule of construction No application that is subject to the requirements of subparagraph (B) shall be subject to the requirements of subparagraph (A), and no application (or supplement to an application) that is subject to the requirements of subparagraph (A) shall be subject to the requirements of subparagraph (B). .\n**(4) Conforming amendments**\nSection 505B(a) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355c(a) ) is amended\u2014\n**(A)**\nin paragraph (3)(C), as redesignated by paragraph (1)(A) of this subsection, by striking investigations described in this paragraph and inserting investigations referred to in subparagraph (A) ; and\n**(B)**\nin paragraph (3)(D), as redesignated by paragraph (1)(A) of this subsection, by striking the assessments under paragraph (2)(B) and inserting the assessments required under paragraph (1)(A) .\n##### (b) Guidance\nThe Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall\u2014\n**(1)**\nnot later than 12 months after the date of enactment of this Act, issue draft guidance on the implementation of the amendments made by subsection (a); and\n**(2)**\nnot later than 12 months after closing the comment period on such draft guidance, finalize such guidance.\n##### (c) Applicability\nThe amendments made by this section apply with respect to any application under section 505(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b) ) and any application under section 351(a) of the Public Health Service Act ( 42 U.S.C. 262(a) ), that is submitted on or after the date that is 3 years after the date of enactment of this Act.\n##### (d) Reports to Congress\n**(1) Secretary of Health and Human Services**\nNot later than 6 years after the date of enactment of this Act, the Secretary of Health and Human Services shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report on the Secretary\u2019s efforts, in coordination with industry, to ensure implementation of the amendments made by subsection (a).\n**(2) GAO study and report**\n**(A) Study**\nNot later than 8 years after the date of enactment of this Act, the Comptroller General of the United States shall conduct a study of the effectiveness of requiring assessments and investigations described in section 505B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355c ), as amended by subsection (a), in the development of drugs and biological products for pediatric cancer indications, including consideration of any benefits to, or burdens on, pediatric cancer drug development.\n**(B) Findings**\nNot later than 10 years after the date of enactment of this Act, the Comptroller General shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report containing the findings of the study conducted under subparagraph (A).\n#### 3. Extension of authority to issue priority review vouchers to encourage treatments for rare pediatric diseases\n##### (a) Extension\nSection 529(b)(5) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360ff(b)(5) ) is amended by striking December 20, 2024, unless and all that follows through the period at the end and inserting September 30, 2029. .\n##### (b) User fee payment\nSubsection 529(c)(4) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360ff(c)(4) ) is amended by striking subparagraph (A) and inserting the following:\n(A) In general The priority review user fee required by this subsection shall be due upon the submission of a human drug application under section 505(b)(1) or section 351(a) of the Public Health Service Act for which the priority review voucher is used. All other user fees associated with the human drug application shall be due as required by the Secretary or under applicable law. .\n##### (c) GAO report on effectiveness of rare pediatric disease priority voucher awards in incentivizing rare pediatric disease drug development\n**(1) GAO study**\n**(A) Study**\nThe Comptroller General of the United States shall conduct a study of the effectiveness of awarding rare pediatric disease priority vouchers under section 529 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360ff ), as amended by subsection (a), in the development of human drug products that treat or prevent rare pediatric diseases (as defined in such section 529).\n**(B) Contents of study**\nIn conducting the study under subparagraph (A), the Comptroller General shall examine the following:\n**(i)**\nThe indications for each drug or biological product that\u2014\n**(I)**\nis the subject of a rare pediatric disease product application (as defined in section 529 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360ff )) for which a priority review voucher was awarded; and\n**(II)**\nwas approved under section 505 of the Federal Food, Drug, and Cosmetic Act ( 42 U.S.C. 355 ) or licensed under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ).\n**(ii)**\nWhether, and to what extent, an unmet need related to the treatment or prevention of a rare pediatric disease was met through the approval or licensure of such a drug or biological product.\n**(iii)**\nThe size of the company to which a priority review voucher was awarded under section 529 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360ff ) for such a drug or biological product.\n**(iv)**\nThe value of such priority review voucher if transferred.\n**(v)**\nIdentification of each drug for which a priority review voucher awarded under such section 529 was used.\n**(vi)**\nThe size of the company using each priority review voucher awarded under such section 529.\n**(vii)**\nThe length of the period of time between the date on which a priority review voucher was awarded under such section 529 and the date on which it was used.\n**(viii)**\nWhether, and to what extent, an unmet need related to the treatment or prevention of a rare pediatric disease was met through the approval under section 505 of the Federal Food, Drug, and Cosmetic Act ( 42 U.S.C. 355 ) or licensure under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) of a drug for which a priority review voucher was used.\n**(ix)**\nWhether, and to what extent, companies were motivated by the availability of priority review vouchers under section 529 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360ff ) to attempt to develop a drug for a rare pediatric disease.\n**(x)**\nWhether, and to what extent, pediatric review vouchers awarded under such section were successful in stimulating development and expedited patient access to drug products for treatment or prevention of a rare pediatric disease that wouldn\u2019t otherwise take place without the incentive provided by such vouchers.\n**(xi)**\nThe impact of such priority review vouchers on the workload, review process, and public health prioritization efforts of the Food and Drug Administration.\n**(xii)**\nAny other incentives in Federal law that exist for companies developing drugs or biological products described in clause (i).\n**(2) Report on findings**\nNot later than 5 years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report containing the findings of the study conducted under paragraph (1).",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-12-02",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3302",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Mikaela Naylon Give Kids a Chance Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-02",
        "text": "Received in the Senate."
      },
      "number": "1262",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Mikaela Naylon Give Kids a Chance Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-31T15:38:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s932",
          "measure-number": "932",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-01-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s932v00",
            "update-date": "2026-01-28"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Give Kids a Chance Act of 2025</strong></p><p>This bill authorizes certain targeted clinical trials involving combinations of drugs to treat pediatric cancer, and renews the Food and Drug Administration\u2019s (FDA\u2019s) authority to award priority review vouchers (PRVs) to sponsors of new products for rare pediatric diseases.</p><p>Specifically, the bill modifies requirements relating to molecularly targeted pediatric cancer investigations to permit research on new drugs used in combination with active ingredients that have already been approved and that (1) have been determined to be part of the standard of care for treating a pediatric cancer, or (2) have been approved to treat an adult cancer and are directed at molecular targets for pediatric cancer.</p><p>The FDA must issue guidance on the implementation of these provisions and report to Congress on its efforts to ensure implementation. The Government Accountability Office (GAO) must report on the effectiveness of the bill's changes with respect to the development of pediatric cancer drugs.</p><p>The bill also renews the FDA\u2019s authority to issue PRVs to sponsors of new products intended to treat rare pediatric diseases through September 30, 2029. This is known as the Rare Pediatric Disease PRV program. The program expired in December 2024.</p><p>GAO must report on the effectiveness of the Rare Pediatric Disease PRV program, including to what extent PRVs were successful in promoting drug development and expediting patient access to drugs for the treatment or prevention of rare pediatric diseases.</p>"
        },
        "title": "Give Kids a Chance Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s932.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Give Kids a Chance Act of 2025</strong></p><p>This bill authorizes certain targeted clinical trials involving combinations of drugs to treat pediatric cancer, and renews the Food and Drug Administration\u2019s (FDA\u2019s) authority to award priority review vouchers (PRVs) to sponsors of new products for rare pediatric diseases.</p><p>Specifically, the bill modifies requirements relating to molecularly targeted pediatric cancer investigations to permit research on new drugs used in combination with active ingredients that have already been approved and that (1) have been determined to be part of the standard of care for treating a pediatric cancer, or (2) have been approved to treat an adult cancer and are directed at molecular targets for pediatric cancer.</p><p>The FDA must issue guidance on the implementation of these provisions and report to Congress on its efforts to ensure implementation. The Government Accountability Office (GAO) must report on the effectiveness of the bill's changes with respect to the development of pediatric cancer drugs.</p><p>The bill also renews the FDA\u2019s authority to issue PRVs to sponsors of new products intended to treat rare pediatric diseases through September 30, 2029. This is known as the Rare Pediatric Disease PRV program. The program expired in December 2024.</p><p>GAO must report on the effectiveness of the Rare Pediatric Disease PRV program, including to what extent PRVs were successful in promoting drug development and expediting patient access to drugs for the treatment or prevention of rare pediatric diseases.</p>",
      "updateDate": "2026-01-28",
      "versionCode": "id119s932"
    },
    "title": "Give Kids a Chance Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Give Kids a Chance Act of 2025</strong></p><p>This bill authorizes certain targeted clinical trials involving combinations of drugs to treat pediatric cancer, and renews the Food and Drug Administration\u2019s (FDA\u2019s) authority to award priority review vouchers (PRVs) to sponsors of new products for rare pediatric diseases.</p><p>Specifically, the bill modifies requirements relating to molecularly targeted pediatric cancer investigations to permit research on new drugs used in combination with active ingredients that have already been approved and that (1) have been determined to be part of the standard of care for treating a pediatric cancer, or (2) have been approved to treat an adult cancer and are directed at molecular targets for pediatric cancer.</p><p>The FDA must issue guidance on the implementation of these provisions and report to Congress on its efforts to ensure implementation. The Government Accountability Office (GAO) must report on the effectiveness of the bill's changes with respect to the development of pediatric cancer drugs.</p><p>The bill also renews the FDA\u2019s authority to issue PRVs to sponsors of new products intended to treat rare pediatric diseases through September 30, 2029. This is known as the Rare Pediatric Disease PRV program. The program expired in December 2024.</p><p>GAO must report on the effectiveness of the Rare Pediatric Disease PRV program, including to what extent PRVs were successful in promoting drug development and expediting patient access to drugs for the treatment or prevention of rare pediatric diseases.</p>",
      "updateDate": "2026-01-28",
      "versionCode": "id119s932"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s932is.xml"
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
      "title": "Give Kids a Chance Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Give Kids a Chance Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act with respect to molecularly targeted pediatric cancer investigations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:14Z"
    }
  ]
}
```
