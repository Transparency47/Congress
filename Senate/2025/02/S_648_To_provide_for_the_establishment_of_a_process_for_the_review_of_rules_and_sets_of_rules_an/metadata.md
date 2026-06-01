# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/648?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/648
- Title: SCRUB Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 648
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2026-02-04T05:06:23Z
- Update date including text: 2026-02-04T05:06:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/648",
    "number": "648",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "SCRUB Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T05:06:23Z",
    "updateDateIncludingText": "2026-02-04T05:06:23Z"
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
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
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
          "date": "2025-02-20T17:36:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s648is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 648\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo provide for the establishment of a process for the review of rules and sets of rules, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Searching for and Cutting Regulations that are Unnecessarily Burdensome Act of 2025 or the SCRUB Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Regulatory Cut-Go\nSec. 101. Cut-go procedures.\nSec. 102. Applicability.\nSec. 103. OIRA certification of cost calculations.\nTITLE II\u2014Retrospective Review of Existing and New Rules\nSec. 201. Plan for review of existing rules.\nSec. 202. Plan for future review.\nTITLE III\u2014Judicial review; effective date\nSec. 301. Judicial review.\nSec. 302. Effective date.\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Office of Information and Regulatory Affairs of the Office of Management and Budget.\n**(2) Agency**\nThe term agency has the meaning given that term in section 551 of title 5, United States Code.\n**(3) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(4) DOGE**\nThe term DOGE means the United States DOGE Service under the Executive Office of the President.\n**(5) Major rule**\nThe term major rule means any rule that the Administrator determines is likely to impose\u2014\n**(A)**\nan annual cost on the economy of $100,000,000 or more, adjusted annually for inflation;\n**(B)**\na major increase in costs or prices for consumers, individual industries, Federal, State, local, or Tribal government agencies, or geographic regions;\n**(C)**\nsignificant adverse effects on competition, employment, investment, productivity, innovation, or on the ability of United States-based enterprises to compete with foreign-based enterprises in domestic and export markets; or\n**(D)**\nsignificant impacts on multiple sectors of the economy.\n**(6) Rule**\nThe term rule has the meaning given that term in section 551 of title 5, United States Code.\n**(7) Set of rules**\nThe term set of rules means a set of rules that collectively implements a regulatory authority of an agency.\nI\nRegulatory Cut-Go\n#### 101. Cut-go procedures\n##### (a) In general\nExcept as provided in section 102, or subsection (b) of this section, when an agency makes a new rule, the agency shall repeal rules or sets of rules of that agency meeting the criteria provided in section 201(d), such that the annual costs of the new rule to the United States economy is offset by such repeals, in an amount equal to or greater than the cost of the new rule, based on the regulatory cost reductions of repeal identified by the DOGE, as calculated pursuant to subsection (d) of this section.\n##### (b) Alternative procedure\n**(1) In general**\nAn agency may, alternatively, repeal rules or sets of rules of that agency meeting the criteria provided in section 201(d) prior to the time specified in subsection (a).\n**(2) Application of reduction of cost**\nIf an agency repeals a rule or set of rules under paragraph (1) and thereby reduces the annual, inflation-adjusted cost of the rule or set of rules to the United States economy, the agency may thereafter apply the reduction in regulatory costs to meet, in whole or in part, the regulatory cost reduction required under subsection (a) to be made at the time the agency promulgates a new rule if the new rule is finalized within 2 years of repeal of the rule or set of rules reducing the annual, inflation-adjusted cost thereof.\n##### (c) Achievement of full net cost reductions\n**(1) In general**\nSubject to the provisions of paragraph (2), an agency may offset the costs of a new rule or set of rules by repealing a rule or set of rules that implement the same statutory authority as the new rule or set of rules.\n**(2) Limitation**\nWhen using the authority provided in paragraph (1), the agency shall achieve a net reduction in costs imposed by the body of rules of the agency (including the new rule or set of rules) that is equal to or greater than the cost of the new rule or set of rules to be promulgated, including, whenever necessary, by repealing additional rules of the agency meeting the criteria provided in section 201(d).\n##### (d) Regulatory cost analysis\nWhen calculating the cost of a new or existing rule for purposes of compliance with this section, an agency shall not consider any non-monetized or unquantified factor.\n#### 102. Applicability\nAn agency shall no longer be subject to the requirements of sections 201 and 203 beginning on the date on which there is no rule or set of rules of the agency meeting the criteria provided in section 201(d) that has not been repealed such that all regulatory cost reductions from repealing rules meeting such criteria have been achieved.\n#### 103. OIRA certification of cost calculations\n##### (a) In general\nThe Administrator shall review and certify the accuracy of agency determinations of the costs of new rules under section 201.\n##### (b) Inclusion\nThe certification described in subsection (a) shall be included in the administrative record of the relevant rulemaking by the agency promulgating the rule, and the Administrator shall transmit a copy of the certification to Congress when the Administrator transmits the certification to the agency.\nII\nRetrospective Review of Existing and New Rules\n#### 201. Plan for review of existing rules\n##### (a) In general\nThe DOGE shall conduct a review of the Code of Federal Regulations to identify and, in coordination with the Director of the Office of Management and Budget and any relevant agency head, repeal rules and sets of rules that collectively implement a regulatory program that should be repealed to lower the cost of regulation to the economy.\n##### (b) Priority\nThe DOGE shall give priority in the review to rules or sets of rules that\u2014\n**(1)**\nare major rules or include major rules;\n**(2)**\nhave been in effect more than 15 years;\n**(3)**\nimpose paperwork burdens that could be reduced substantially without significantly diminishing regulatory effectiveness;\n**(4)**\nimpose disproportionately high costs on entities that qualify as small entities within the meaning of section 601(6) of title 5, United States Code; or\n**(5)**\ncould be strengthened in their effectiveness while reducing regulatory costs.\n##### (c) Goal\nThe DOGE shall have as a goal to achieve a reduction of at least 33 percent in the cumulative costs of Federal regulation with a minimal reduction in the overall effectiveness of such regulation by no later than July 4, 2026, by coordinating with the Director, the Administrator, and relevant agency heads to repeal rules or sets of rules identified pursuant to subsection (d) of this section.\n##### (d) Nature of review\nTo identify which rules and sets of rules should be repealed to lower the cost of regulation to the economy, the DOGE shall apply the following criteria:\n**(1)**\nWhether the original purpose of the rule or set of rules was achieved, and the rule or set of rules could be repealed without significant recurrence of adverse effects or conduct that the rule or set of rules was intended to prevent or reduce.\n**(2)**\nWhether the implementation, compliance, administration, enforcement or other costs of the rule or set of rules to the economy are not justified by the benefits to society within the United States that are directly attributable to the rule or set of rules produced by the expenditure of those costs.\n**(3)**\nWhether the rule or set of rules has been rendered unnecessary or obsolete, taking into consideration the length of time since the rule was made and the degree to which technology, economic conditions, market practices, or other relevant factors have changed in the subject area affected by the rule or set of rules.\n**(4)**\nWhether the rule or set of rules is ineffective at achieving the purposes of the rule or set of rules when evaluated using data analytics and statistical relationships, or unable to be evaluated using such standards.\n**(5)**\nWhether the rule or set of rules overlaps, duplicates, or conflicts with other Federal rules, and to the extent feasible, with State and local governmental rules.\n**(6)**\nWhether the rule or set of rules has excessive compliance costs or is otherwise excessively burdensome, as compared to alternatives that\u2014\n**(A)**\nspecify performance objectives rather than conduct or manners of compliance;\n**(B)**\nestablish economic incentives to encourage desired behavior;\n**(C)**\nprovide information upon which choices can be made by the public;\n**(D)**\nincorporate other innovative alternatives rather than agency actions that specify conduct or manners of compliance; or\n**(E)**\ncould in other ways substantially lower costs without significantly undermining effectiveness.\n**(7)**\nWhether the rule or set of rules inhibits innovation in or growth of the United States economy, such as by impeding the introduction or use of safer or equally safe technology that is newer or more efficient than technology required by or permissible under the rule or set of rules.\n**(8)**\nWhether or not the rule or set of rules harms competition within the United States economy or the international economic competitiveness of enterprises or entities based in the United States.\n**(9)**\nWhether the rule or set of rules concerns a major economic or policy question but lacks an explicit statutory basis.\n**(10)**\nWhether the rule or set of rules imposes costs or burdens disproportionately and predominantly on one segment of society or one industry if the benefits of such rule or set of rules accrue to a distinct segment of society or industry.\n**(11)**\nWhether the rule or set of rules is justified in whole or in part by a benefit accrued by one or more foreign nations while costs are borne by American consumers, businesses, other entities, or individuals.\n**(12)**\nWhether the rule or set of rules are not based on the best meaning and plain reading of the enabling statute for the rule or set of rules.\n**(13)**\nSuch other criteria as the DOGE devises to identify rules and sets of rules that can be repealed to eliminate or reduce unnecessarily burdensome costs to the United States economy.\n##### (e) No substantially similar rule To be reissued\nA rule that is repealed under subsection (a) of this section or section 101 may not be reissued in substantially the same form, and a new rule that is substantially the same as such a rule may not be issued, unless the reissued or new rule is specifically authorized by a law enacted after the date of the repeal of the original rule.\n#### 202. Plan for future review\n##### (a) In general\nWhen an agency makes a rule, the agency shall include in the final issuance of such rule a plan for the review of such rule by not later than 10 years after the date such rule is made.\n##### (b) Review of rules\nThe plan for review under subsection (a) shall use interpretations and definitions of terms included in 201(d) that are substantially similar to those used by the DOGE under the review pursuant to section 201.\n##### (c) Public comment on plan\nWhenever feasible, an agency shall include a proposed plan for review of a proposed rule under subsection (a) in the notice of proposed rulemaking for the rule and shall receive public comment on the plan.\n##### (d) Repeal of rules\nThe Director of the Office of Management and Budget, in coordination with any relevant agency head, shall repeal any rule failing to meet the criteria provided section 201(d).\nIII\nJudicial review; effective date\n#### 301. Judicial review\n##### (a) Cut-Go procedures\nAgency non-compliance with title I shall be subject to judicial review under chapter 7 of title 5, United States Code.\n##### (b) Plans for future review\nAgency non-compliance with section 202 shall be subject to judicial review under chapter 7 of title 5, United States Code.\n#### 302. Effective date\nThis Act and the amendments made by this Act shall take effect beginning on the date of enactment of this Act.",
      "versionDate": "2025-02-20",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-07-10T14:45:56Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-07-10T14:46:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-06T20:55:45Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s648is.xml"
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
      "title": "SCRUB Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SCRUB Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Searching for and Cutting Regulations that are Unnecessarily Burdensome Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the establishment of a process for the review of rules and sets of rules, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:33Z"
    }
  ]
}
```
