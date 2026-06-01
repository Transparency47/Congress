# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4658?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4658
- Title: STUDENT Act
- Congress: 119
- Bill type: HR
- Bill number: 4658
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-12-05T22:03:29Z
- Update date including text: 2025-12-05T22:03:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4658",
    "number": "4658",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "F000471",
        "district": "5",
        "firstName": "Scott",
        "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
        "lastName": "Fitzgerald",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "STUDENT Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:03:29Z",
    "updateDateIncludingText": "2025-12-05T22:03:29Z"
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
          "date": "2025-07-23T14:13:50Z",
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
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "WI"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "WI"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "WA"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "MD"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "FL"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "SC"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4658ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4658\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Fitzgerald (for himself, Mr. Grothman , Ms. Lee of Florida , Mr. Gooden , Mr. Finstad , and Mr. Tiffany ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend chapter 1511 of title 36, United States Code, to impose certain requirements on the National Education Association, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Teachers Unions from Damaging Education Needs Today Act or the STUDENT Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe National Education Association (referred to in this section as the NEA ) was chartered in 1906 by an Act of Congress (34 Stat. 804, chapter 3929) to elevate the character and advance the interests of the profession of teaching; and to promote the cause of education in the United States ( 36 U.S.C. 151102 ) and remains the only labor union that has a Federal charter.\n**(2)**\nBy continuing to hold its Federal charter, the NEA\u2019s actions and advocacy effectively receive Congress\u2019 seal of approval.\n**(3)**\nThe NEA can no longer be considered a patriotic or national organization worthy of its Federal charter as it has drifted substantially from its core mission and become a massive political operation dedicated to electing Democrats and imposing a radical progressive agenda on the schools of the United States.\n**(4)**\nIn July 2019, NEA members held an assembly and voted against adding a business item to the organization that stated: The National Education Association will rededicate itself to the pursuit of increased student learning in every public school in America by putting a renewed emphasis on quality education. NEA will make student learning the priority of the association .\n**(5)**\nIn the same assembly, NEA members voted in support of the right to an abortion, supporting illegal immigration, and expanding professional development for educators to help create student Gender Sexuality Alliance clubs.\n**(6)**\nAccording to disclosures made to the Office of Labor-Management Standards, from September 2019 to August 2021, the NEA spent over $116,700,000 on political activities and lobbying, and in the 2020 election cycle, 95.7 percent of candidate campaign contributions by the NEA went to Democrat candidates.\n**(7)**\nThe NEA adopted measures in July 2021 to support critical race theory, calling it reasonable and appropriate , and to spend $56,500 on researching and shaming organizations fighting the inclusion of critical race theory in schools.\n**(8)**\nThe NEA and other teacher unions stood in the way of reopening schools in 2020 and 2021 by threatening strikes, donating to Democrat candidates that backed school closures, and influencing Centers for Disease Control and Prevention guidance to make it harder for schools to reopen.\n**(9)**\nIn July 2025, NEA members held an assembly and voted to cut ties with the Anti-Defamation League (referred to in this section as the ADL ) due to the ADL\u2019s position on Israel and countering antisemitism. Cutting ties would mean no longer using ADL materials on antisemitism and Holocaust education nor promoting the ADL\u2019s statistics or programs.\n**(10)**\nAt the same assembly, the NEA members voted to refer to President Donald J. Trump\u2019s policies as fascism .\n#### 3. Membership classification\nSection 151103 of title 36, United States Code, is amended to read as follows:\n151103. Membership (a) In general Except as otherwise provided in this section, eligibility for membership in the corporation and the rights, obligations, and designation of classes of members are as provided in the bylaws. (b) Collection of dues from State or local government employees The corporation and its State and local affiliates may only accept payment of membership dues or fees from an employee of a State or local government (as such terms are defined in section 3371 of title 5) either directly from the employee or indirectly via per capita taxes or other fees paid by an affiliate, if\u2014 (1) the employee has been notified by the corporation or its applicable State or local affiliate of their right under the First Amendment to the Constitution of the United States to refrain from membership and payment of associated dues or fees; (2) the employee has clearly and affirmatively consented to membership and payment of associated dues or fees; and (3) the employee has authorized the transmittal of the employee's membership dues or fees to the corporation or its applicable State or local affiliate without the use, directly or indirectly, of payroll deduction. (c) Membership cancellation The corporation and its State or local affiliates shall process and honor membership and dues payment cancellation requests as soon as practicable following receipt. .\n#### 4. Requirements\nSection 151105 of title 36, United States Code, is amended\u2014\n**(1)**\nin the matter before paragraph (1), by striking The and inserting (a) Powers.\u2014 The ; and\n**(2)**\nby adding at the end the following:\n(b) Requirements The corporation shall comply with the following requirements: (1) The corporation, or a director or officer of the corporation as such, may not contribute to, support, or participate in any political activity or in any manner attempt to influence legislation. (2) The corporation and its State or local affiliates shall not\u2014 (A) discriminate against individuals on the basis of race, color, religion, sex, disability, age, or national origin; or (B) establish or observe any quota based on race, color, religion, sex, disability, age, or national origin in matters concerning membership, corporate governance, or personnel. (3) Each officer of the corporation shall be a citizen of the United States. (4) The corporation shall maintain its status as an organization exempt from taxation under the Internal Revenue Code of 1986. (5) The form of government of the corporation must be representative of the membership-at-large and may not permit concentration of control in a limited number of members or in a self-perpetuating group not representative of the membership-at-large. (6) The corporation is liable for any act of any officer or agent of the corporation acting within the scope of the authority of the corporation. (7) The corporation shall comply with the law governing service of process in\u2014 (A) the District of Columbia; (B) each State in which it is incorporated; and (C) each State in which it carries out activities. (8) The corporation shall keep\u2014 (A) correct and complete records of account; (B) minutes of the proceedings of members, board of directors, and committees of the corporation having any of the authority of the board of directors of the corporation; and (C) at the principal office of the corporation established under section 151107 of this title, a record of the names and addresses of the members of the corporation entitled to vote on matters relating to the corporation. (9) A member entitled to vote on any matter relating to the corporation, or an agent or attorney of the member, may inspect the records of the corporation for any proper purpose at any time. (10) The corporation shall submit to Congress an annual report on the activities of the corporation during the preceding fiscal year. (11) The Attorney General of the United States may bring a civil action in the United States District Court for the District of Columbia for appropriate equitable relief if the corporation\u2014 (A) engages or threatens to engage in any act, practice, or policy that is inconsistent with the purposes described in section 151102 of this title; or (B) refuses, fails, or neglects to carry out its obligations under this chapter or threatens to do so. (12) On dissolution or final liquidation of the corporation, any assets remaining after the discharge or satisfactory provision for the discharge of all liabilities shall be either deposited in the Treasury of the United States as a miscellaneous receipt or divided equally among employed individuals who are, at the time of dissolution or final liquidation, members of the corporation or any of its State or local affiliates. (13) No part of the compensation received for work performed on behalf of the corporation, or any of its State or local affiliates, by any officer or representative of the corporation, or any of its State or local affiliates, who is an employee of a State or local government (as such terms are defined in section 3371 of title 5), may be derived from payments made by the State or local government to the corporation or its officers or representatives. (14) The corporation and its State or local affiliates shall not\u2014 (A) require or encourage staff, officers, affiliates, or members to affirm, adopt, or adhere to any belief of concept that\u2014 (i) the United States is fundamentally or irredeemably racist or sexist; (ii) an individual, by virtue of sex, race, ethnicity, religion, color, or national origin\u2014 (I) is inherently racist, sexist, or oppressive, whether consciously or unconsciously; or (II) should be blamed for actions committed in the past by other members of the same sex, race, ethnicity, religion, color, or national origin; (iii) an individual\u2019s moral character is necessarily determined, in whole or in part, by the sex, race, ethnicity, religion, color, or national origin of the individual; or (iv) promotes antisemitic beliefs or practices, including beliefs that perpetuate harmful stereotypes about Jewish people, deny or minimize the Holocaust, or promote hatred or discrimination against Jewish individuals based on identity, ancestry or connection to and beliefs about Israel; or (B) advocate for or encourage any local educational agency, public school (including a public charter school), or governmental entity responsible for the oversight of public secondary or elementary schools to require students to affirm, adopt, or adhere to any of the beliefs, practices, or concepts described in subparagraph (A). (15) The corporation and its State or local affiliates shall not\u2014 (A) call, or participate in, a strike, work stoppage, or slowdown affecting a State or local government (as such terms are defined in section 3371 of title 5); or (B) condone any activity described in subparagraph (A) of this paragraph by failing to take action to prevent or stop such activity. (16) The corporation and each of its State and local affiliates shall be deemed to be a labor organization, as such term is defined in section 3 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 402 ), and shall abide by all provisions of such Act applicable to labor organizations. .\n#### 5. Repeal of District of Columbia property tax exemption\n##### (a) In general\nSection 151106 of title 36, United States Code, is repealed.\n##### (b) Conforming amendment\nThe analysis for chapter 1511 of title 36, United States Code, is amended by repealing the item relating to section 151106.",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2428",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STUDENT Act",
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
        "name": "Education",
        "updateDate": "2025-09-12T18:12:17Z"
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
          "measure-id": "id119hr4658",
          "measure-number": "4658",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2025-11-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4658v00",
            "update-date": "2025-11-18"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stopping Teachers Unions from Damaging Education Needs Today Act or the STUDENT Act</strong></p><p>This bill revises the federal charter for the National Education Association.</p><p>The bill specifies that\u00a0the corporation and its state and local affiliates may only accept payment of membership dues or fees from a state or local government employee if the employee (1) has been notified of the employee's right under the First Amendment to refrain from membership and payment of associated dues or fees, (2) has clearly and affirmatively consented to membership and payment of associated dues or fees, and (3) has authorized the transmittal of membership dues or fees without the use of payroll deduction.</p><p>Further, the corporation and its state or local affiliates must process and honor cancellation requests for membership or payment of dues as soon as practicable following receipt of the request.</p><p>The bill also outlines requirements for the corporation, such as\u00a0</p><ul><li>prohibiting the corporation or its directors or officers from contributing to, supporting, or participating in political activities;</li><li>requiring each officer of the corporation to be a U.S. citizen;\u00a0</li><li>requiring the corporation to submit annual reports to Congress;</li><li>prohibiting the corporation and its affiliates from requiring staff, officers, affiliates, or members to affirm, adopt, or adhere to certain principles related to race or sex; and</li><li>prohibiting the corporation and its affiliates from calling or participating in a strike, work stoppage, or slowdown affecting a state or local government.</li></ul><p>The bill repeals the corporation's exemption from District of Columbia property taxes.</p>"
        },
        "title": "STUDENT Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4658.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stopping Teachers Unions from Damaging Education Needs Today Act or the STUDENT Act</strong></p><p>This bill revises the federal charter for the National Education Association.</p><p>The bill specifies that\u00a0the corporation and its state and local affiliates may only accept payment of membership dues or fees from a state or local government employee if the employee (1) has been notified of the employee's right under the First Amendment to refrain from membership and payment of associated dues or fees, (2) has clearly and affirmatively consented to membership and payment of associated dues or fees, and (3) has authorized the transmittal of membership dues or fees without the use of payroll deduction.</p><p>Further, the corporation and its state or local affiliates must process and honor cancellation requests for membership or payment of dues as soon as practicable following receipt of the request.</p><p>The bill also outlines requirements for the corporation, such as\u00a0</p><ul><li>prohibiting the corporation or its directors or officers from contributing to, supporting, or participating in political activities;</li><li>requiring each officer of the corporation to be a U.S. citizen;\u00a0</li><li>requiring the corporation to submit annual reports to Congress;</li><li>prohibiting the corporation and its affiliates from requiring staff, officers, affiliates, or members to affirm, adopt, or adhere to certain principles related to race or sex; and</li><li>prohibiting the corporation and its affiliates from calling or participating in a strike, work stoppage, or slowdown affecting a state or local government.</li></ul><p>The bill repeals the corporation's exemption from District of Columbia property taxes.</p>",
      "updateDate": "2025-11-18",
      "versionCode": "id119hr4658"
    },
    "title": "STUDENT Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stopping Teachers Unions from Damaging Education Needs Today Act or the STUDENT Act</strong></p><p>This bill revises the federal charter for the National Education Association.</p><p>The bill specifies that\u00a0the corporation and its state and local affiliates may only accept payment of membership dues or fees from a state or local government employee if the employee (1) has been notified of the employee's right under the First Amendment to refrain from membership and payment of associated dues or fees, (2) has clearly and affirmatively consented to membership and payment of associated dues or fees, and (3) has authorized the transmittal of membership dues or fees without the use of payroll deduction.</p><p>Further, the corporation and its state or local affiliates must process and honor cancellation requests for membership or payment of dues as soon as practicable following receipt of the request.</p><p>The bill also outlines requirements for the corporation, such as\u00a0</p><ul><li>prohibiting the corporation or its directors or officers from contributing to, supporting, or participating in political activities;</li><li>requiring each officer of the corporation to be a U.S. citizen;\u00a0</li><li>requiring the corporation to submit annual reports to Congress;</li><li>prohibiting the corporation and its affiliates from requiring staff, officers, affiliates, or members to affirm, adopt, or adhere to certain principles related to race or sex; and</li><li>prohibiting the corporation and its affiliates from calling or participating in a strike, work stoppage, or slowdown affecting a state or local government.</li></ul><p>The bill repeals the corporation's exemption from District of Columbia property taxes.</p>",
      "updateDate": "2025-11-18",
      "versionCode": "id119hr4658"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4658ih.xml"
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
      "title": "STUDENT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STUDENT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Teachers Unions from Damaging Education Needs Today Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 1511 of title 36, United States Code, to impose certain requirements on the National Education Association, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:34Z"
    }
  ]
}
```
