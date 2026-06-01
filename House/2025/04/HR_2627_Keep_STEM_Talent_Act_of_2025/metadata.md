# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2627?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2627
- Title: Keep STEM Talent Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2627
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-05-22T08:07:37Z
- Update date including text: 2026-05-22T08:07:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2627",
    "number": "2627",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Keep STEM Talent Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:37Z",
    "updateDateIncludingText": "2026-05-22T08:07:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:01:30Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NY"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "DC"
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
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "TX"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "NM"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "DE"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MI"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "OH"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "TN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "VA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "NM"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "WA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NC"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2627ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2627\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Foster (for himself, Mr. Lawler , Ms. Houlahan , and Ms. Norton ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide lawful permanent resident status for certain advanced STEM degree holders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Keep STEM Talent Act of 2025 .\n#### 2. Visa requirements\n##### (a) Graduate degree visa requirements\nTo be approved for or maintain nonimmigrant status under section 101(a)(15)(F) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F) ), a student seeking to pursue an advanced degree in a STEM field (as defined in section 201(b)(1)(F)(ii) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1)(F)(ii) )) (as amended by section 3(a)) for a degree at the master\u2019s level or higher at a United States institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ) must apply for admission prior to beginning such advanced degree program.\n##### (b) Strengthened vetting process\nThe Secretary of Homeland Security and the Secretary of State shall establish procedures to ensure that aliens described in subsection (a) are admissible pursuant to section 212(a)(3)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3)(A) ). Such procedures shall ensure that such aliens seeking admission from within the United States undergo verification of academic credentials, comprehensive background checks, and interviews in a manner equivalent to that of an alien seeking admission from outside of the United States. To the greatest extent practicable, the Secretary of Homeland Security and the Secretary of State shall also take steps to ensure that such applications for admission are processed in a timely manner to allow the pursuit of graduate education.\n##### (c) Reporting requirement\nThe Secretary of Homeland Security and the Secretary of State shall submit an annual report to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives detailing the implementation and effectiveness of the requirement for foreign graduate students pursuing advanced degrees in STEM fields to seek admission prior to pursuing a graduate degree program. The report shall include data on visa application volumes, processing times, security outcomes, and economic impacts.\n#### 3. Lawful permanent resident status for certain advanced stem degree holders\n##### (a) Aliens not subject to direct numerical limitations\nSection 201(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1) ) is amended by adding at the end the following:\n(F) (i) Aliens who\u2014 (I) have earned a degree in a STEM field at the master\u2019s level or higher while physically present in the United States from a United States institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) accredited by an accrediting entity recognized by the Department of Education; (II) have an offer of employment from, or are employed by, a United States employer to perform work that is directly related to such degree at a rate of pay that is higher than the median wage level for the occupational classification in the area of employment, as determined by the Secretary of Labor; and (III) have an approved labor certification under section 212(a)(5)(A)(i); or (IV) are the spouses and children of aliens described in subclauses (I) through (III) who are accompanying or following to join such aliens. (ii) In this subparagraph, the term STEM field means a field of science, technology, engineering, or mathematics described in the most recent version of the Classification of Instructional Programs of the Department of Education taxonomy under the summary group of\u2014 (I) computer and information sciences and support services; (II) engineering; (III) mathematics and statistics; (IV) biological and biomedical sciences; (V) physical sciences; (VI) agriculture sciences; or (VII) natural resources and conservation sciences. .\n##### (b) Procedure for granting immigration status\nSection 204(a)(1)(F) of the Immigration and Nationality Act ( 8 U.S.C. 1154(a)(1)(F) ) is amended\u2014\n**(1)**\nby striking 203(b)(2) and all that follows through Attorney General ; and\n**(2)**\nby inserting 203(b)(2), 203(b)(3), or 201(b)(1)(F) may file a petition with the Secretary of Homeland Security .\n##### (c) Labor certification\nSection 212(a)(5)(D) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(5)(D) ) is amended by inserting section 201(b)(1)(F) or under after adjustment of status under .\n##### (d) Dual intent for F nonimmigrants seeking advanced STEM degrees at United States institutions of higher education\nNotwithstanding sections 101(a)(15)(F)(i) and 214(b) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F)(i) and 1184(b)), an alien who is a bona fide student admitted to a program in a STEM field (as defined in subparagraph (F)(ii) of section 201(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1) )) for a degree at the master\u2019s level or higher at a United States institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) accredited by an accrediting entity recognized by the Department of Education may obtain a student visa, be admitted to the United States as a nonimmigrant student, or extend or change nonimmigrant status to pursue such degree even if such alien seeks lawful permanent resident status in the United States. Nothing in this subsection may be construed to modify or amend section 101(a)(15)(F)(i) or 214(b) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F)(i) or 1184(b)), or any regulation interpreting these authorities for an alien who is not described in this subsection.",
      "versionDate": "2025-04-03",
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
        "actionDate": "2025-04-01",
        "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S2095-2096)"
      },
      "number": "1233",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keep STEM Talent Act of 2025",
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
        "name": "Immigration",
        "updateDate": "2025-04-10T12:26:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119hr2627",
          "measure-number": "2627",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-03",
          "originChamber": "HOUSE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2627v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keep STEM Talent Act of 2025</strong></p><p>This bill addresses issues relating to non-U.S. nationals (<em>aliens</em> under federal law) with advanced degrees in a science, technology, engineering, or mathematics (STEM) field, including exempting certain such individuals from direct limitations on the number of immigrant visas granted per year.</p><p>To be exempt from the annual numerical limitations on immigrant visas, the individual must (1) have earned a master's level or higher degree in certain STEM fields while in the United States attending an accredited higher education institution, (2) be employed (or have an offer) to perform work directly related to the degree and earn higher than the median wage for that occupation, and (3) meet certain labor certification requirements.</p><p>The bill also allows an individual seeking a nonimmigrant F-1 (student) visa for an advanced STEM degree to obtain the nonimmigrant visa even if the individual seeks lawful permanent resident status. (Generally, an individual may be denied a nonimmigrant visa if the individual actually intends to seek immigrant status, unless dual intent is allowed for that visa.)</p><p>Under this bill, to be approved for an F-1 visa for an advanced STEM degree, the applicant must apply for the visa before beginning the advanced degree program.</p><p>The bill also requires an individual who is inside the United States and applying for an F-1 visa for an advanced STEM degree to undergo the same vetting (e.g., verifying academic credentials and undergoing background checks) as an individual applying from outside the United States.</p>"
        },
        "title": "Keep STEM Talent Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2627.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep STEM Talent Act of 2025</strong></p><p>This bill addresses issues relating to non-U.S. nationals (<em>aliens</em> under federal law) with advanced degrees in a science, technology, engineering, or mathematics (STEM) field, including exempting certain such individuals from direct limitations on the number of immigrant visas granted per year.</p><p>To be exempt from the annual numerical limitations on immigrant visas, the individual must (1) have earned a master's level or higher degree in certain STEM fields while in the United States attending an accredited higher education institution, (2) be employed (or have an offer) to perform work directly related to the degree and earn higher than the median wage for that occupation, and (3) meet certain labor certification requirements.</p><p>The bill also allows an individual seeking a nonimmigrant F-1 (student) visa for an advanced STEM degree to obtain the nonimmigrant visa even if the individual seeks lawful permanent resident status. (Generally, an individual may be denied a nonimmigrant visa if the individual actually intends to seek immigrant status, unless dual intent is allowed for that visa.)</p><p>Under this bill, to be approved for an F-1 visa for an advanced STEM degree, the applicant must apply for the visa before beginning the advanced degree program.</p><p>The bill also requires an individual who is inside the United States and applying for an F-1 visa for an advanced STEM degree to undergo the same vetting (e.g., verifying academic credentials and undergoing background checks) as an individual applying from outside the United States.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hr2627"
    },
    "title": "Keep STEM Talent Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep STEM Talent Act of 2025</strong></p><p>This bill addresses issues relating to non-U.S. nationals (<em>aliens</em> under federal law) with advanced degrees in a science, technology, engineering, or mathematics (STEM) field, including exempting certain such individuals from direct limitations on the number of immigrant visas granted per year.</p><p>To be exempt from the annual numerical limitations on immigrant visas, the individual must (1) have earned a master's level or higher degree in certain STEM fields while in the United States attending an accredited higher education institution, (2) be employed (or have an offer) to perform work directly related to the degree and earn higher than the median wage for that occupation, and (3) meet certain labor certification requirements.</p><p>The bill also allows an individual seeking a nonimmigrant F-1 (student) visa for an advanced STEM degree to obtain the nonimmigrant visa even if the individual seeks lawful permanent resident status. (Generally, an individual may be denied a nonimmigrant visa if the individual actually intends to seek immigrant status, unless dual intent is allowed for that visa.)</p><p>Under this bill, to be approved for an F-1 visa for an advanced STEM degree, the applicant must apply for the visa before beginning the advanced degree program.</p><p>The bill also requires an individual who is inside the United States and applying for an F-1 visa for an advanced STEM degree to undergo the same vetting (e.g., verifying academic credentials and undergoing background checks) as an individual applying from outside the United States.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hr2627"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2627ih.xml"
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
      "title": "Keep STEM Talent Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T05:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep STEM Talent Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide lawful permanent resident status for certain advanced STEM degree holders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T05:48:23Z"
    }
  ]
}
```
