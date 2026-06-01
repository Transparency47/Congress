# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2401?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2401
- Title: 287(g) Program Protection Act
- Congress: 119
- Bill type: S
- Bill number: 2401
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-09-16T15:26:52Z
- Update date including text: 2025-09-16T15:26:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2401",
    "number": "2401",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "287(g) Program Protection Act",
    "type": "S",
    "updateDate": "2025-09-16T15:26:52Z",
    "updateDateIncludingText": "2025-09-16T15:26:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T16:41:43Z",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "ID"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "UT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "KS"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "WV"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2401is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2401\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Risch (for himself, Mr. Crapo , Mr. Lee , Mr. Marshall , Mr. Justice , Mr. Scott of Florida , and Mr. Johnson ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 287(g) of the Immigration and Nationality Act to clarify congressional intent with respect to agreements under such section, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 287(g) Program Protection Act .\n#### 2. Clarification of congressional intent\nSection 287(g) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g) ) is amended\u2014\n**(1)**\nby amending paragraph (1) to read as follows:\n(1) (A) Notwithstanding section 1342 of title 31, United States Code, the Secretary of Homeland Security shall enter into a written agreement with a State, or any political subdivision of a State, upon request of the State or political subdivision, pursuant to which law enforcement officers of such State or subdivision, who the Secretary determines are qualified to perform a function of an immigration officer in relation to the investigation, apprehension, or detention of aliens in the United States (including the transportation of such aliens across State lines to detention centers), may carry out such function at the expense of the State or political subdivision. (B) All requests described in subparagraph (A) from a bona fide State or political subdivision or a bona fide law enforcement agency shall be approved absent a compelling reason. If the Secretary denies a request described in subparagraph (A), the Secretary, not later than 180 days before finalizing such denial, shall\u2014 (i) submit to Congress an explanation containing the reasons for denying such request; and (ii) publish such explanation in the Federal Register. (C) The Secretary may not place any limit on the number of agreements that may be approved under this subsection. The Secretary shall process each request for such an agreement as expeditiously as possible and never later than the date that is 90 days after the date on which the request is received. (D) In this subsection, any reference to a political subdivision shall be construed to include any law enforcement or corrections agency of such political subdivision. ;\n**(2)**\nby striking Attorney General each place such term appears and inserting Secretary ;\n**(3)**\nby redesignating paragraphs (2) through (10) as paragraphs (5) through (13), respectively;\n**(4)**\nby inserting after paragraph (1) the following:\n(2) An agreement under this subsection shall accommodate a requesting State or political subdivision with respect to the enforcement model or combination of models, and shall accommodate a patrol model, task force model, jail model, any combination thereof, or any other reasonable model the State or political subdivision believes is best suited to the immigration enforcement needs of its jurisdiction. (3) No Federal program or technology directed broadly at identifying inadmissible or deportable aliens shall substitute for such agreements, including those establishing a jail model, and shall operate in addition to any agreement under this subsection. (4) (A) No agreement under this subsection may be terminated absent a compelling reason. (B) (i) The Secretary shall provide a State or political subdivision written notice of intent to terminate at least 180 days prior to date of intended termination, and the notice shall fully explain the grounds for termination, along with providing evidence substantiating the Secretary\u2019s allegations. (ii) In order to determine whether the requirements of this paragraph have been satisfied, the State or political subdivision shall have the right\u2014 (I) to appeal the decision of the Secretary to an administrative law judge for a hearing and decision; or (II) to bring a civil action in an appropriate court of jurisdiction. (C) The agreement shall remain in full effect during the course of any and all legal proceedings. ; and\n**(5)**\nin paragraph (6), as redesignated, by adding at the end the following: The Secretary of Homeland Security shall implement uniform training requirements for law enforcement officers who are, or will be, performing a function of an immigration officer authorized under this subsection. The training requirements shall align with Federal Law Enforcement Training Center standards for training under this subsection (as in effect on the date of the enactment of the 287(g) Program Protection Act ). .\n#### 3. Funding\nSection 286(r) of the Immigration and Nationality Act ( 8 U.S.C. 1356(r) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking Breached Bond/Detention Fund and inserting Breached Bond/Detention/287 (g) Fund ;\n**(2)**\nby striking Attorney General each place such term appears and inserting Secretary of Homeland Security ;\n**(3)**\nin paragraph (1), by striking Breached Bond/Detention and inserting Breached Bond/Detention/287(g) ;\n**(4)**\nin paragraph (2), by striking Department of Justice, and amount described in section 245(i)(3)(b) and inserting Department of Homeland Security, and the amount described in section 245(i)(3)(B) ; and\n**(5)**\nin paragraph (3)\u2014\n**(A)**\nin clause (i), by striking , and at the end and inserting a semicolon;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iv) for expenses associated with administering section 287(g). .\n#### 4. Annual performance report and recruitment plan\n##### (a) Annual performance report\nNot later than December 31 of the first fiscal year that begins after the date of the enactment of this Act, and not later than December 31 of each year thereafter, the Secretary of Homeland Security shall publish an annual performance report on the program authorized under section 287(g) of the Immigration and Nationality Act, as amended by section 2, which includes\u2014\n**(1)**\nthe number of aliens apprehended and screened by law enforcement through such program;\n**(2)**\nthe number of aliens removed from the United States as a result of the program;\n**(3)**\nthe number of aliens described in paragraph (1) who were not removed and an explanation for why they were not removed;\n**(4)**\nthe methods being used to conduct oversight of each law enforcement agency participating under the program;\n**(5)**\nthe number of law enforcement agencies in compliance with the program\u2019s training requirements;\n**(6)**\nthe number of complaints filed against law enforcement agencies claiming they did not comply their written agreement entered into under such section;\n**(7)**\nthe number of law enforcement agencies that had such written agreement terminated; and\n**(8)**\nthe reasons for such termination.\n##### (b) Annual recruitment plan\nNot later than December 31 of the first fiscal year that begins after the date of the enactment of this Act, and not later than December 31 of each year thereafter, the Secretary of Homeland Security shall publish an annual recruitment plan with respect to the program authorized under section 287(g) of the Immigration and Nationality Act, as amended by section 2, which includes\u2014\n**(1)**\nannual goals for the following 5 years with respect to the recruitment of new States and political subdivisions of States to participate in the program;\n**(2)**\nthe number of new States and political subdivisions of States participating in the program during each year;\n**(3)**\na description of the outreach to States and political subdivisions of States conducted for the program and the other methods used to achieve recruitment goals; and\n**(4)**\nthe number of requests for agreements that\u2014\n**(A)**\nwere received during the reporting period;\n**(B)**\nwere approved during the reporting period;\n**(C)**\nwere denied during the reporting period; or\n**(D)**\nare pending approval as of the last day of the reporting period.\n#### 5. Rulemaking\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Homeland Security shall publish a notice of rulemaking with respect to the training requirements under section 287(g)(6) of the Immigration and Nationality Act, as added by section 2(5).",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-09-16T15:26:52Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2401is.xml"
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
      "title": "287(g) Program Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "287(g) Program Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 287(g) of the Immigration and Nationality Act to clarify congressional intent with respect to agreements under such section, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:24Z"
    }
  ]
}
```
