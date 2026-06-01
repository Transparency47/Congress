# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5238?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5238
- Title: Stop Super PAC-Candidate Coordination Act
- Congress: 119
- Bill type: HR
- Bill number: 5238
- Origin chamber: House
- Introduced date: 2025-09-09
- Update date: 2026-04-23T08:06:46Z
- Update date including text: 2026-04-23T08:06:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-09: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-09-09: Introduced in House

## Actions

- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5238",
    "number": "5238",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Stop Super PAC-Candidate Coordination Act",
    "type": "HR",
    "updateDate": "2026-04-23T08:06:46Z",
    "updateDateIncludingText": "2026-04-23T08:06:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T14:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "MI"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MN"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "PA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CA"
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
      "sponsorshipDate": "2026-04-22",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5238ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5238\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 9, 2025 Mrs. Ramirez (for herself, Mr. Mullin , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act to clarify the treatment of coordinated expenditures as contributions made to candidates under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Super PAC-Candidate Coordination Act .\n#### 2. Clarification of treatment of coordinated expenditures as contributions to candidates\n##### (a) Treatment as contribution to candidate\nSection 301(8)(A) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101(8)(A) ) is amended\u2014\n**(1)**\nby striking or at the end of clause (i);\n**(2)**\nby striking the period at the end of clause (ii) and inserting ; or ; and\n**(3)**\nby adding at the end the following new clause:\n(iii) any payment made by any person (other than a candidate, an authorized committee of a candidate, or a political committee of a political party) for a coordinated expenditure (as such term is defined in section 325) which is not otherwise treated as a contribution under clause (i) or clause (ii). .\n##### (b) Definitions\nTitle III of such Act ( 52 U.S.C. 30101 et seq. ) is amended by adding at the end the following new section:\n325. Payments for coordinated expenditures (a) Coordinated expenditures (1) In general For purposes of section 301(8)(A)(iii), the term coordinated expenditure means\u2014 (A) any expenditure, or any payment for a covered communication described in subsection (d), which is made in cooperation, consultation, or concert with, or at the request or suggestion of, a candidate, an authorized committee of a candidate, a political committee of a political party, or agents of the candidate or committee, as defined in subsection (b); or (B) any payment for any communication which republishes, disseminates, or distributes, in whole or in part, any video or broadcast or any written, graphic, or other form of campaign material prepared by the candidate or committee or by agents of the candidate or committee (including any excerpt or use of any video from any such broadcast or written, graphic, or other form of campaign material). (2) Exception for payments for certain communications A payment for a communication (including a covered communication described in subsection (d)) shall not be treated as a coordinated expenditure under this subsection if\u2014 (A) the communication appears in a news story, commentary, or editorial distributed through the facilities of any broadcasting station, newspaper, magazine, or other periodical publication, unless such facilities are owned or controlled by any political party, political committee, or candidate; or (B) the communication constitutes a candidate debate or forum conducted pursuant to regulations adopted by the Commission pursuant to section 304(f)(3)(B)(iii), or which solely promotes such a debate or forum and is made by or on behalf of the person sponsoring the debate or forum. (b) Coordination described (1) In general For purposes of this section, a payment is made in cooperation, consultation, or concert with, or at the request or suggestion of, a candidate, an authorized committee of a candidate, a political committee of a political party, or agents of the candidate or committee, if the payment, or any communication for which the payment is made, is not made entirely independently of the candidate, committee, or agents. For purposes of the previous sentence, a payment or communication not made entirely independently of the candidate or committee includes any payment or communication made pursuant to any general or particular understanding with, or pursuant to any communication with, the candidate, committee, or agents about the payment or communication. (2) No finding of coordination based solely on sharing of information regarding legislative or policy position For purposes of this section, a payment shall not be considered to be made by a person in cooperation, consultation, or concert with, or at the request or suggestion of, a candidate or committee, solely on the grounds that the person or the person\u2019s agent engaged in discussions with the candidate or committee, or with any agent of the candidate or committee, regarding that person's position on a legislative or policy matter (including urging the candidate or committee to adopt that person's position), so long as there is no communication between the person and the candidate or committee, or any agent of the candidate or committee, regarding the candidate\u2019s or committee\u2019s campaign advertising, message, strategy, policy, polling, allocation of resources, fundraising, or other campaign activities. (3) No effect on party coordination standard Nothing in this section shall be construed to affect the determination of coordination between a candidate and a political committee of a political party for purposes of section 315(d). (4) No safe harbor for use of firewall A person shall be determined to have made a payment in cooperation, consultation, or concert with, or at the request or suggestion of, a candidate or committee, in accordance with this section without regard to whether or not the person established and used a firewall or similar procedures to restrict the sharing of information between individuals who are employed by or who are serving as agents for the person making the payment. (c) Payments by coordinated spenders for covered communications (1) Payments made in cooperation, consultation, or concert with candidates For purposes of subsection (a)(1)(A), if the person who makes a payment for a covered communication, as defined in subsection (d), is a coordinated spender under paragraph (2) with respect to the candidate as described in subsection (d)(1), the payment for the covered communication is made in cooperation, consultation, or concert with the candidate. (2) Coordinated spender defined For purposes of this subsection, the term coordinated spender means, with respect to a candidate or an authorized committee of a candidate, a person (other than a political committee of a political party) for which any of the following applies: (A) During the 4-year period ending on the date on which the person makes the payment, the person was directly or indirectly formed or established by or at the request or suggestion of, or with the encouragement of, the candidate (including an individual who later becomes a candidate) or committee or agents of the candidate or committee, including with the approval of the candidate or committee or agents of the candidate or committee. (B) The candidate or committee or any agent of the candidate or committee solicits funds, appears at a fundraising event, or engages in other fundraising activity on the person\u2019s behalf during the election cycle involved, including by providing the person with names of potential donors or other lists to be used by the person in engaging in fundraising activity, regardless of whether the person pays fair market value for the names or lists provided. For purposes of this subparagraph, the term election cycle means, with respect to an election for Federal office, the period beginning on the day after the date of the most recent general election for that office (or, if the general election resulted in a runoff election, the date of the runoff election) and ending on the date of the next general election for that office (or, if the general election resulted in a runoff election, the date of the runoff election). (C) The person is established, directed, or managed by the candidate or committee or by any person who, during the 4-year period ending on the date on which the person makes the payment, has been employed or retained as a political, campaign media, or fundraising adviser or consultant for the candidate or committee or for any other entity directly or indirectly controlled by the candidate or committee, or has held a formal position with the candidate or committee (including a position as an employee of the office of the candidate at any time the candidate held any Federal, State, or local public office during the 4-year period). (D) The person has retained the professional services of any person who, during the 2-year period ending on the date on which the person makes the payment, has provided or is providing professional services relating to the campaign to the candidate or committee, without regard to whether the person providing the professional services used a firewall. For purposes of this subparagraph, the term professional services includes any services in support of the candidate\u2019s or committee\u2019s campaign activities, including advertising, message, strategy, policy, polling, allocation of resources, fundraising, and campaign operations, but does not include accounting or legal services. (E) The person is established, directed, or managed by a member of the immediate family of the candidate, or the person or any officer or agent of the person has had more than incidental discussions about the candidate\u2019s campaign with a member of the immediate family of the candidate. For purposes of this subparagraph, the term immediate family has the meaning given such term in section 9004(e) of the Internal Revenue Code of 1986. (d) Covered communication defined (1) In general For purposes of this section, the term covered communication means, with respect to a candidate or an authorized committee of a candidate, a public communication (as defined in section 301(22)) which\u2014 (A) expressly advocates the election of the candidate or the defeat of an opponent of the candidate (or contains the functional equivalent of express advocacy); (B) promotes or supports the election of the candidate, or attacks or opposes the election of an opponent of the candidate (regardless of whether the communication expressly advocates the election or defeat of a candidate or contains the functional equivalent of express advocacy); or (C) refers to the candidate or an opponent of the candidate but is not described in subparagraph (A) or subparagraph (B), but only if the communication is disseminated during the applicable election period. (2) Applicable election period In paragraph (1)(C), the applicable election period with respect to a communication means\u2014 (A) in the case of a communication which refers to a candidate in a general, special, or runoff election, the 120-day period which ends on the date of the election; or (B) in the case of a communication which refers to a candidate in a primary or preference election, or convention or caucus of a political party that has authority to nominate a candidate, the 60-day period which ends on the date of the election or convention or caucus. (3) Special rules for communications involving congressional candidates For purposes of this subsection, a public communication shall not be considered to be a covered communication with respect to a candidate for election for an office other than the office of President or Vice President unless it is publicly disseminated or distributed in the jurisdiction of the office the candidate is seeking. (e) Penalty (1) Determination of amount Any person who knowingly and willfully commits a violation of this Act by making a contribution which consists of a payment for a coordinated expenditure shall be fined an amount equal to the greater of\u2014 (A) in the case of a person who makes a contribution which consists of a payment for a coordinated expenditure in an amount exceeding the applicable contribution limit under this Act, 300 percent of the amount by which the amount of the payment made by the person exceeds such applicable contribution limit; or (B) in the case of a person who is prohibited under this Act from making a contribution in any amount, 300 percent of the amount of the payment made by the person for the coordinated expenditure. (2) Joint and several liability Any director, manager, or officer of a person who is subject to a penalty under paragraph (1) shall be jointly and severally liable for any amount of such penalty that is not paid by the person prior to the expiration of the 1-year period which begins on the date the Commission imposes the penalty or the 1-year period which begins on the date of the final judgment following any judicial review of the Commission\u2019s action, whichever is later. .\n##### (c) Effective date\n**(1) Repeal of existing regulations on coordination**\nEffective upon the expiration of the 90-day period which begins on the date of the enactment of this Act\u2014\n**(A)**\nthe regulations on coordinated communications adopted by the Federal Election Commission which are in effect on the date of the enactment of this Act (as set forth in 11 CFR Part 109, Subpart C, under the heading Coordination ) are repealed; and\n**(B)**\nthe Federal Election Commission shall promulgate new regulations on coordinated communications which reflect the amendments made by this Act.\n**(2) Effective date**\nThe amendments made by this section shall apply with respect to payments made on or after the expiration of the 120-day period which begins on the date of the enactment of this Act, without regard to whether or not the Federal Election Commission has promulgated regulations in accordance with paragraph (1)(B) as of the expiration of such period.\n#### 3. Clarification of ban on fundraising for super PACs by Federal candidates and officeholders\n##### (a) In General\nSection 323(e)(1) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30125(e)(1) ) is amended\u2014\n**(1)**\nby striking or at the end of subparagraph (A);\n**(2)**\nby striking the period at the end of subparagraph (B) and inserting ; or ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(C) solicit, receive, direct, or transfer funds to or on behalf of any political committee which accepts donations or contributions that do not comply with the limitations, prohibitions, and reporting requirements of this Act (or to or on behalf of any account of a political committee which is established for the purpose of accepting such donations or contributions), or to or on behalf of any political organization under section 527 of the Internal Revenue Code of 1986 which accepts such donations or contributions (other than a committee of a State or local political party or a candidate for election for State or local office). .\n##### (b) Effective Date\nThe amendment made by subsection (a) shall apply with respect to elections occurring after January 1, 2026.",
      "versionDate": "2025-09-09",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-18T15:44:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-09",
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
          "measure-id": "id119hr5238",
          "measure-number": "5238",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-09",
          "originChamber": "HOUSE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5238v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-09-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Super PAC-Candidate Coordination Act</strong></p><p>This bill treats certain payments for coordinated expenditures as campaign contributions for purposes of disclosure and reporting requirements.</p><p>The bill generally defines a\u00a0<em>coordinated expenditure</em> as a payment made by any person in cooperation with a candidate, an authorized committee of a candidate, a political committee of a political party, or an agent of a candidate or committee. Further, the bill sets forth penalties for willfully violating limits related to making contributions to a candidate for coordinated expenditures.</p><p>The bill also prohibits a candidate or an individual holding federal office from soliciting, receiving, directing, or transferring funds to or on behalf of certain types of political committees.</p>"
        },
        "title": "Stop Super PAC-Candidate Coordination Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5238.xml",
    "summary": {
      "actionDate": "2025-09-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Super PAC-Candidate Coordination Act</strong></p><p>This bill treats certain payments for coordinated expenditures as campaign contributions for purposes of disclosure and reporting requirements.</p><p>The bill generally defines a\u00a0<em>coordinated expenditure</em> as a payment made by any person in cooperation with a candidate, an authorized committee of a candidate, a political committee of a political party, or an agent of a candidate or committee. Further, the bill sets forth penalties for willfully violating limits related to making contributions to a candidate for coordinated expenditures.</p><p>The bill also prohibits a candidate or an individual holding federal office from soliciting, receiving, directing, or transferring funds to or on behalf of certain types of political committees.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr5238"
    },
    "title": "Stop Super PAC-Candidate Coordination Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Super PAC-Candidate Coordination Act</strong></p><p>This bill treats certain payments for coordinated expenditures as campaign contributions for purposes of disclosure and reporting requirements.</p><p>The bill generally defines a\u00a0<em>coordinated expenditure</em> as a payment made by any person in cooperation with a candidate, an authorized committee of a candidate, a political committee of a political party, or an agent of a candidate or committee. Further, the bill sets forth penalties for willfully violating limits related to making contributions to a candidate for coordinated expenditures.</p><p>The bill also prohibits a candidate or an individual holding federal office from soliciting, receiving, directing, or transferring funds to or on behalf of certain types of political committees.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr5238"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5238ih.xml"
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
      "title": "Stop Super PAC-Candidate Coordination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T06:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Super PAC-Candidate Coordination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act to clarify the treatment of coordinated expenditures as contributions made to candidates under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T06:48:36Z"
    }
  ]
}
```
