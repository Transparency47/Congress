# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/481?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/481
- Title: Securing our Border Act
- Congress: 119
- Bill type: S
- Bill number: 481
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-12-19T21:55:50Z
- Update date including text: 2025-12-19T21:55:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/481",
    "number": "481",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Securing our Border Act",
    "type": "S",
    "updateDate": "2025-12-19T21:55:50Z",
    "updateDateIncludingText": "2025-12-19T21:55:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T22:16:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "LA"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "SD"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s481is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 481\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Scott of South Carolina (for himself, Mr. Cassidy , Mr. Rounds , and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo reprogram all remaining unobligated funds from the IRS enforcement account.\n#### 1. Short title\nThis Act may be cited as the Securing our Border Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nUnited States border security is paramount to the general welfare of our Nation and ensures the efficient and meaningful flow of goods and individuals through legal means.\n**(2)**\nDuring 2023, an estimated 105,007 drug overdose deaths occurred in the United States.\n**(3)**\nOnly 2 percent of passenger vehicles and 20 percent of commercial vehicles crossing the southern border are scanned by nonintrusive inspection technology through a radiation portal monitor.\n**(4)**\nDuring fiscal year 2023, U.S. Customs and Border Protection agents processed more than 1,081,030 passengers and pedestrians.\n**(5)**\nLimiting the amount of deadly illicit narcotics, including fentanyl, from entering the United States would reduce the number of Americans who die annually from the use of such narcotics.\n**(6)**\nBecause of the failure to update nonintrusive inspection technologies at land ports of entry along the southern border of the United States, there has been an increase in the amount of illicit narcotics, such as fentanyl, being trafficked across the southern border.\n**(7)**\nThe amount of illicit drugs seized by U.S. Customs and Border Protection along the southwest border was approximately\u2014\n**(A)**\n241,000 pounds during fiscal year 2023; and\n**(B)**\n275,000 pounds during fiscal year 2024.\n**(8)**\nU.S. Customs and Border Protection agents had 2,135,005 encounters along the southern border during fiscal year 2024, including\u2014\n**(A)**\n1,218,880 single adults;\n**(B)**\n804,456 family units; and\n**(C)**\n109,998 unaccompanied minors.\n**(9)**\nAccording to the Department of Homeland Security, 750 migrants died attempting to cross the southern border during fiscal year 2022, which is\u2014\n**(A)**\nmore migrant deaths than occurred in any previous fiscal year; and\n**(B)**\nmore than 200 more migrant deaths than the number of such deaths during fiscal year 2021.\n**(10)**\nAs of September 30, 2024, the immigration court backlog was 3,558,995 cases.\n**(11)**\nSince the end of fiscal year 2019, U.S. Customs and Border Protection has reported 2,371 encounters with potential terrorists at ports of entry along the southern and northern borders.\n**(12)**\nAccording to U.S. Customs and Border Protection onboard staffing data, approximately 2,700 additional U.S. Customs and Border Protection officers need to be stationed at United States ports of entry to fully staff such ports.\n**(13)**\nDue to shifting priorities, construction delays, a lack of available technology solutions, and funding constraints, most southern U.S. Border Patrol sectors still rely on obsolete systems or technologies.\n#### 3. Funding for nonintrusive border inspections\nOne-third of the unobligated balances (as of the date of the enactment of this Act) from amounts made available under section 10301(1)(A)(ii) of Public Law 117\u2013169 shall be transferred to U.S. Customs and Border Protection during the period beginning on the date of the enactment of this Act and ending on February 6, 2034, for nonintrusive inspection systems to achieve a 100 percent nonintrusive inspection scanning rate at all northern border and southwest border land ports of entry by February 6, 2034.\n#### 4. Funding for border wall construction\n##### (a) In general\nTwo-thirds of the unobligated balances (as of the date of the enactment of this Act) from amounts made available under section 10301(1)(A)(ii) of Public Law 117\u2013169 shall be transferred to the Department of Homeland Security during the period beginning on the date of the enactment of this Act and ending on February 6, 2034, for activities related to the construction of a border wall system along the southwest international border of the United States.\n##### (b) Quarterly reports\nThe Secretary of Homeland Security shall submit quarterly reports to the Committee on Appropriations of the Senate , the Committee on Finance of the Senate , the Committee on Homeland Security and Governmental Affairs of the Senate , the Committee on Appropriations of the House of Representatives , the Committee on Ways and Means of the House of Representatives , and the Committee on Homeland Security of the House of Representatives that contains\u2014\n**(1)**\nan implementation plan with benchmarks related to stemming illegal immigration; and\n**(2)**\ncost estimates associated with border wall system construction.\n#### 5. Authorization to provide bonuses to U.S. Customs and Border Protection agents\n##### (a) Recruitment bonuses\n**(1) In general**\nSubject to the approval of the Secretary of Homeland Security, the Commissioner of U.S. Customs and Border Protection may pay a recruitment bonus, not to exceed $15,000, to each newly hired U.S. Customs and Border Protection agent after\u2014\n**(A)**\nthe agent completes initial basic training; and\n**(B)**\nthe execution of a written agreement described in paragraph (2).\n**(2) Written agreement**\nA written agreement described in this paragraph is a legally binding agreement between a newly hired agent and U.S. Customs and Border Protection that\u2014\n**(A)**\nspecifies the amount of the bonus payment to be paid to such agent, including the timing of such payment;\n**(B)**\nthe length of the period of service required to be completed before such agent is entitled to retain such payment; and\n**(C)**\nany other terms and conditions to which such payment is subject.\n##### (b) Retention bonuses\nSubject to the approval of the Secretary of Homeland Security, the Commissioner of U.S. Customs and Border Protection may pay annual retention bonuses, not to exceed 15 percent of the agent's basic pay, to U.S. Border Patrol agents after the completion of each year of satisfactory service, as determined by the Commissioner.\n##### (c) Relocation bonus\nSubject to the approval of the Secretary of Homeland Security, the Commissioner of U.S. Customs and Border Protection may pay a relocation bonus, not to exceed 15 percent of the agent's annual basic pay, to a U.S. Customs and Border Protection agent who agrees to be transferred and to serve for not less than 3 years at the new duty station.\n##### (d) Limitation\nNone of the bonuses paid to a U.S. Customs and Border Protection agent pursuant to subsections (a) through (c) may be considered part of the basic pay of such agent for any purpose, including for retirement or in computing a lump-sum payment to the agent for accumulated and accrued annual leave under section 5551 or 5552 of title 5, United States Code.\n#### 6. Treatment of aliens arriving from contiguous territory\nSection 235(b)(2)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(2)(C) ) is amended by striking may return and all that follows and inserting the following:\nshall\u2014 (i) return the alien to such territory, or to a safe third country (as described in section 208), pending the completion of a proceeding under section 240; or (ii) detain the alien for further consideration of an application for asylum, which shall include a determination of credible fear of persecution. .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-07-25",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Homeland Security, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4765",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Securing our Border Act",
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
        "updateDate": "2025-03-12T14:17:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s481",
          "measure-number": "481",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-12-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s481v00",
            "update-date": "2025-12-19"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Securing our Border Act</strong></p><p>This bill addresses issues concerning border security and immigration, including by transferring unobligated funds from the Internal Revenue Service to certain border-related projects.</p><p>Specifically, the bill transfers certain unobligated funds previously appropriated for tax enforcement activities (e.g., collecting owed taxes and conducting criminal investigations) to fund (1) nonintrusive inspection systems along the northern border and southwest border of the United States, and (2) the construction of a border wall system along the southwest border.</p><p>The bill also authorizes the U.S. Customs and Border Protection to pay recruitment, retention, and relocation bonuses, subject to various requirements and limitations. For example, a relocation bonus may not exceed 15% of the agent's annual basic bay and must be conditioned on the agent agreeing to serve for at least three years at the new duty station.</p><p>The bill also modifies the treatment of non-U.S. nationals (<em>aliens</em> under federal law) arriving by land from a country next to the United States. Specifically, if such an individual is not clearly entitled to admission into the United States, the Department of Justice must (1) return the individual to that neighboring country or a safe third country while removal proceedings are pending, or (2) detain the individual while the individual's asylum application is under consideration. (Current law authorizes DOJ to return the individual to the neighboring country but does not require such action or detention.)</p>"
        },
        "title": "Securing our Border Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s481.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Securing our Border Act</strong></p><p>This bill addresses issues concerning border security and immigration, including by transferring unobligated funds from the Internal Revenue Service to certain border-related projects.</p><p>Specifically, the bill transfers certain unobligated funds previously appropriated for tax enforcement activities (e.g., collecting owed taxes and conducting criminal investigations) to fund (1) nonintrusive inspection systems along the northern border and southwest border of the United States, and (2) the construction of a border wall system along the southwest border.</p><p>The bill also authorizes the U.S. Customs and Border Protection to pay recruitment, retention, and relocation bonuses, subject to various requirements and limitations. For example, a relocation bonus may not exceed 15% of the agent's annual basic bay and must be conditioned on the agent agreeing to serve for at least three years at the new duty station.</p><p>The bill also modifies the treatment of non-U.S. nationals (<em>aliens</em> under federal law) arriving by land from a country next to the United States. Specifically, if such an individual is not clearly entitled to admission into the United States, the Department of Justice must (1) return the individual to that neighboring country or a safe third country while removal proceedings are pending, or (2) detain the individual while the individual's asylum application is under consideration. (Current law authorizes DOJ to return the individual to the neighboring country but does not require such action or detention.)</p>",
      "updateDate": "2025-12-19",
      "versionCode": "id119s481"
    },
    "title": "Securing our Border Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Securing our Border Act</strong></p><p>This bill addresses issues concerning border security and immigration, including by transferring unobligated funds from the Internal Revenue Service to certain border-related projects.</p><p>Specifically, the bill transfers certain unobligated funds previously appropriated for tax enforcement activities (e.g., collecting owed taxes and conducting criminal investigations) to fund (1) nonintrusive inspection systems along the northern border and southwest border of the United States, and (2) the construction of a border wall system along the southwest border.</p><p>The bill also authorizes the U.S. Customs and Border Protection to pay recruitment, retention, and relocation bonuses, subject to various requirements and limitations. For example, a relocation bonus may not exceed 15% of the agent's annual basic bay and must be conditioned on the agent agreeing to serve for at least three years at the new duty station.</p><p>The bill also modifies the treatment of non-U.S. nationals (<em>aliens</em> under federal law) arriving by land from a country next to the United States. Specifically, if such an individual is not clearly entitled to admission into the United States, the Department of Justice must (1) return the individual to that neighboring country or a safe third country while removal proceedings are pending, or (2) detain the individual while the individual's asylum application is under consideration. (Current law authorizes DOJ to return the individual to the neighboring country but does not require such action or detention.)</p>",
      "updateDate": "2025-12-19",
      "versionCode": "id119s481"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s481is.xml"
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
      "title": "Securing our Border Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing our Border Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reprogram all remaining unobligated funds from the IRS enforcement account.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:39Z"
    }
  ]
}
```
