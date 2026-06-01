# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1233?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1233
- Title: Keep STEM Talent Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1233
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2026-01-22T17:36:27Z
- Update date including text: 2026-01-22T17:36:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S2095-2096)
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S2095-2096)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1233",
    "number": "1233",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Keep STEM Talent Act of 2025",
    "type": "S",
    "updateDate": "2026-01-22T17:36:27Z",
    "updateDateIncludingText": "2026-01-22T17:36:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S2095-2096)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T20:20:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "SD"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-01",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1233is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1233\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Durbin (for himself, Mr. Rounds , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide lawful permanent resident status for certain advanced STEM degree holders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Keep STEM Talent Act of 2025 .\n#### 2. Visa requirements\n##### (a) Graduate degree visa requirements\nTo be approved for or maintain nonimmigrant status under section 101(a)(15)(F) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F) ), a student seeking to pursue an advanced degree in a STEM field (as defined in section 201(b)(1)(F)(ii) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1)(F)(ii) )) (as amended by section 3(a)) for a degree at the master\u2019s level or higher at a United States institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ) must apply for admission prior to beginning such advanced degree program.\n##### (b) Strengthened vetting process\nThe Secretary of Homeland Security and the Secretary of State shall establish procedures to ensure that aliens described in subsection (a) are admissible pursuant to section 212(a)(3)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3)(A) ). Such procedures shall ensure that such aliens seeking admission from within the United States undergo verification of academic credentials, comprehensive background checks, and interviews in a manner equivalent to that of an alien seeking admission from outside of the United States. To the greatest extent practicable, the Secretary of Homeland Security and the Secretary of State shall also take steps to ensure that such applications for admission are processed in a timely manner to allow the pursuit of graduate education.\n##### (c) Reporting requirement\nThe Secretary of Homeland Security and the Secretary of State shall submit an annual report to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives detailing the implementation and effectiveness of the requirement for foreign graduate students pursuing advanced degrees in STEM fields to seek admission prior to pursuing a graduate degree program. The report shall include data on visa application volumes, processing times, security outcomes, and economic impacts.\n#### 3. Lawful permanent resident status for certain advanced stem degree holders\n##### (a) Aliens not subject to direct numerical limitations\nSection 201(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1) ) is amended by adding at the end the following:\n(F) (i) Aliens who\u2014 (I) have earned a degree in a STEM field at the master\u2019s level or higher while physically present in the United States from a United States institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) accredited by an accrediting entity recognized by the Department of Education; (II) have an offer of employment from, or are employed by, a United States employer to perform work that is directly related to such degree at a rate of pay that is higher than the median wage level for the occupational classification in the area of employment, as determined by the Secretary of Labor; (III) have an approved labor certification under section 212(a)(5)(A)(i); or (IV) are the spouses and children of aliens described in subclauses (I) through (III) who are accompanying or following to join such aliens. (ii) In this subparagraph, the term STEM field means a field of science, technology, engineering, or mathematics described in the most recent version of the Classification of Instructional Programs of the Department of Education taxonomy under the summary group of\u2014 (I) computer and information sciences and support services; (II) engineering; (III) mathematics and statistics; (IV) biological and biomedical sciences; (V) physical sciences; (VI) agriculture sciences; or (VII) natural resources and conservation sciences. .\n##### (b) Procedure for granting immigration status\nSection 204(a)(1)(F) of the Immigration and Nationality Act ( 8 U.S.C. 1154(a)(1)(F) ) is amended by striking 203(b)(2) and all that follows through Attorney General and inserting 203(b)(2), 203(b)(3), or 201(b)(1)(F) may file a petition with the Secretary of Homeland Security .\n##### (c) Labor certification\nSection 212(a)(5)(D) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(5)(D) ) is amended by inserting section 201(b)(1)(F) or under after adjustment of status under .\n##### (d) Dual intent for F nonimmigrants seeking advanced STEM degrees at United States institutions of higher education\n**(1) In general**\nNotwithstanding sections 101(a)(15)(F)(i) and 214(b) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F)(i) and 1184(b)), an alien who is a bona fide student admitted to a program in a STEM field (as defined in subparagraph (F)(ii) of section 201(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1) )) for a degree at the master\u2019s level or higher at a United States institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) accredited by an accrediting entity recognized by the Department of Education may obtain a student visa, be admitted to the United States as a nonimmigrant student, or extend or change nonimmigrant status to pursue such degree even if such alien seeks lawful permanent resident status in the United States.\n**(2) Rule of construction**\nNothing in this subsection may be construed to modify or amend section 101(a)(15)(F)(i) or 214(b) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F)(i) or 1184(b)), or any regulation interpreting such authorities for an alien who is not described in this subsection.",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2627",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keep STEM Talent Act of 2025",
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
        "name": "Immigration",
        "updateDate": "2025-05-01T15:01:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119s1233",
          "measure-number": "1233",
          "measure-type": "s",
          "orig-publish-date": "2025-04-01",
          "originChamber": "SENATE",
          "update-date": "2026-01-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1233v00",
            "update-date": "2026-01-22"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Keep STEM Talent Act of 2025</strong></p><p>This bill addresses issues relating to non-U.S. nationals (<em>aliens</em> under federal law) with advanced degrees in a science, technology, engineering, or mathematics (STEM) field, including exempting certain such individuals from direct limitations on the number of immigrant visas granted per year.</p><p>To be exempt from the annual numerical limitations on immigrant visas, the individual must (1) have earned a master's level or higher degree in certain STEM fields while in the United States attending an accredited higher education institution, (2) be employed (or have an offer) to perform work directly related to the degree and earn higher than the median wage for that occupation, and (3) meet certain labor certification requirements.</p><p>The bill also allows an individual seeking a nonimmigrant F-1 (student) visa for an advanced STEM degree to obtain the nonimmigrant visa even if the individual seeks lawful permanent resident status. (Generally, an individual may be denied a nonimmigrant visa if the individual actually intends to seek immigrant status, unless dual intent is allowed for that visa.)</p><p>Under this bill, to be approved for an F-1 visa for an advanced STEM degree, the applicant must apply for the visa before beginning the advanced degree program.</p><p>The bill also requires an individual who is inside the United States and applying for an F-1 visa for an advanced STEM degree to undergo the same vetting (e.g., verifying academic credentials and undergoing background checks) as an individual applying from outside the United States.</p>"
        },
        "title": "Keep STEM Talent Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1233.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keep STEM Talent Act of 2025</strong></p><p>This bill addresses issues relating to non-U.S. nationals (<em>aliens</em> under federal law) with advanced degrees in a science, technology, engineering, or mathematics (STEM) field, including exempting certain such individuals from direct limitations on the number of immigrant visas granted per year.</p><p>To be exempt from the annual numerical limitations on immigrant visas, the individual must (1) have earned a master's level or higher degree in certain STEM fields while in the United States attending an accredited higher education institution, (2) be employed (or have an offer) to perform work directly related to the degree and earn higher than the median wage for that occupation, and (3) meet certain labor certification requirements.</p><p>The bill also allows an individual seeking a nonimmigrant F-1 (student) visa for an advanced STEM degree to obtain the nonimmigrant visa even if the individual seeks lawful permanent resident status. (Generally, an individual may be denied a nonimmigrant visa if the individual actually intends to seek immigrant status, unless dual intent is allowed for that visa.)</p><p>Under this bill, to be approved for an F-1 visa for an advanced STEM degree, the applicant must apply for the visa before beginning the advanced degree program.</p><p>The bill also requires an individual who is inside the United States and applying for an F-1 visa for an advanced STEM degree to undergo the same vetting (e.g., verifying academic credentials and undergoing background checks) as an individual applying from outside the United States.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119s1233"
    },
    "title": "Keep STEM Talent Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keep STEM Talent Act of 2025</strong></p><p>This bill addresses issues relating to non-U.S. nationals (<em>aliens</em> under federal law) with advanced degrees in a science, technology, engineering, or mathematics (STEM) field, including exempting certain such individuals from direct limitations on the number of immigrant visas granted per year.</p><p>To be exempt from the annual numerical limitations on immigrant visas, the individual must (1) have earned a master's level or higher degree in certain STEM fields while in the United States attending an accredited higher education institution, (2) be employed (or have an offer) to perform work directly related to the degree and earn higher than the median wage for that occupation, and (3) meet certain labor certification requirements.</p><p>The bill also allows an individual seeking a nonimmigrant F-1 (student) visa for an advanced STEM degree to obtain the nonimmigrant visa even if the individual seeks lawful permanent resident status. (Generally, an individual may be denied a nonimmigrant visa if the individual actually intends to seek immigrant status, unless dual intent is allowed for that visa.)</p><p>Under this bill, to be approved for an F-1 visa for an advanced STEM degree, the applicant must apply for the visa before beginning the advanced degree program.</p><p>The bill also requires an individual who is inside the United States and applying for an F-1 visa for an advanced STEM degree to undergo the same vetting (e.g., verifying academic credentials and undergoing background checks) as an individual applying from outside the United States.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119s1233"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1233is.xml"
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
      "title": "Keep STEM Talent Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keep STEM Talent Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide lawful permanent resident status for certain advanced STEM degree holders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:18:29Z"
    }
  ]
}
```
