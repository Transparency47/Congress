# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/30?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/30
- Title: ERASER Act
- Congress: 119
- Bill type: S
- Bill number: 30
- Origin chamber: Senate
- Introduced date: 2025-01-08
- Update date: 2025-07-11T18:06:13Z
- Update date including text: 2025-07-11T18:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-08: Introduced in Senate
- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-08: Introduced in Senate

## Actions

- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-08",
    "latestAction": {
      "actionDate": "2025-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/30",
    "number": "30",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "ERASER Act",
    "type": "S",
    "updateDate": "2025-07-11T18:06:13Z",
    "updateDateIncludingText": "2025-07-11T18:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-08",
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
      "actionDate": "2025-01-08",
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
          "date": "2025-01-08T16:27:06Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "FL"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s30is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 30\nIN THE SENATE OF THE UNITED STATES\nJanuary 8, 2025 Mr. Schmitt (for himself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require each agency to repeal 3 existing regulations before issuing a new regulation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expediting Reform And Stopping Excess Regulations Act or the ERASER Act .\n#### 2. Definitions\nIn this Act:\n**(1) Agency; rule**\nThe terms agency and rule have the meanings given those terms in section 551 of title 5, United States Code.\n**(2) Major rule**\nThe term major rule has the meaning given the term in section 804 of title 5, United States Code.\n**(3) State**\nThe term State means each of the several States, the District of Columbia, each territory or possession of the United States, and each federally recognized Indian tribe.\n#### 3. Repeal of regulations required before issuance of a new rule\n##### (a) Requirement for rule\nAn agency may not issue a rule unless the agency has repealed 3 or more rules described in subsection (c) that, to the extent practicable, are related to the rule.\n##### (b) Requirement for major rule\n**(1) Repeal required**\nAn agency may not issue a major rule unless\u2014\n**(A)**\nthe agency has repealed 3 or more rules described in subsection (c) that, to the extent practicable, are related to the major rule; and\n**(B)**\nthe cost of the new major rule is less than or equal to the cost of the rules repealed.\n**(2) Certified cost**\nFor any rule issued in accordance with paragraph (1), the Administrator of the Office of Information and Regulatory Affairs of the Office of Management and Budget shall certify that the cost of the new major rule is equal to or less than the cost of the rules repealed.\n##### (c) Repealed rules described\nA rule described in this subsection\u2014\n**(1)**\ndoes not include an interpretative rule, general statement of policy, or rule of agency organization, procedure, or practice; and\n**(2)**\nwas issued through the notice and comment rulemaking process under section 553 of title 5, United States Code.\n##### (d) Publication required\nAny rule repealed under subsection (a) or (b) shall be published in the Federal Register.\n##### (e) Applicability\nThis section\u2014\n**(1)**\napplies to any rule or major rule that imposes a cost or responsibility on a nongovernmental person or a State or local government; and\n**(2)**\nshall not apply to any rule or major rule that relates to the management, organization, or personnel of an agency or procurement by the agency.\n#### 4. Government Accountability Office study of rules\nNot later than 1 year after the date of enactment of this Act, and every 5 years thereafter, the Comptroller General of the United States shall conduct a study and submit to Congress a report that includes, as of the date on which the report is submitted\u2014\n**(1)**\nthe number of rules that are in effect;\n**(2)**\nthe number of major rules that are in effect; and\n**(3)**\nthe total estimated economic cost imposed by the rules described in paragraphs (1) and (2).",
      "versionDate": "2025-01-08",
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
            "updateDate": "2025-03-05T16:07:24Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-05T16:07:40Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-05T16:07:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-27T16:22:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-08",
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
          "measure-id": "id119s30",
          "measure-number": "30",
          "measure-type": "s",
          "orig-publish-date": "2025-01-08",
          "originChamber": "SENATE",
          "update-date": "2025-03-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s30v00",
            "update-date": "2025-03-20"
          },
          "action-date": "2025-01-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Expediting Reform And Stopping Excess Regulations Act or the ERASER Act</strong></p><p>This bill generally requires federal agencies to repeal three rules before issuing a new rule.</p><p>In the case of a new nonmajor rule, an agency must repeal at least three rules that, to the extent practicable, are related to the new rule.</p><p>In the case of a new major rule, (1) an agency must repeal at least three rules\u00a0that are related to the new major rule, and (2) the cost of the new major rule must be less than or equal to the cost of the repealed rules.\u00a0A\u00a0<em>major rule</em> is a rule that has resulted in or is likely to result in (1) an annual effect on the economy of $100 million or more; (2) a major increase in costs or prices for consumers, individual industries, government agencies, or geographic regions; or (3) significant adverse effects on competition, employment, investment, productivity, or innovation.</p><p>These requirements apply to rules issued through the notice and comment process and do not apply to interpretative rules, general statements of policy, or rules of agency organization, procedure, or practice. Further, the requirements do not apply to a rule or major rule that relates to the management, organization, or personnel of an agency or procurement by the agency.</p><p>Any rule repealed under this bill must\u00a0be published in the Federal Register.</p><p>Finally, the Government Accountability Office must report on\u00a0the number and estimated cost of rules and major rules currently in effect.</p><p>\u00a0</p><p>\u00a0</p>"
        },
        "title": "ERASER Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s30.xml",
    "summary": {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expediting Reform And Stopping Excess Regulations Act or the ERASER Act</strong></p><p>This bill generally requires federal agencies to repeal three rules before issuing a new rule.</p><p>In the case of a new nonmajor rule, an agency must repeal at least three rules that, to the extent practicable, are related to the new rule.</p><p>In the case of a new major rule, (1) an agency must repeal at least three rules\u00a0that are related to the new major rule, and (2) the cost of the new major rule must be less than or equal to the cost of the repealed rules.\u00a0A\u00a0<em>major rule</em> is a rule that has resulted in or is likely to result in (1) an annual effect on the economy of $100 million or more; (2) a major increase in costs or prices for consumers, individual industries, government agencies, or geographic regions; or (3) significant adverse effects on competition, employment, investment, productivity, or innovation.</p><p>These requirements apply to rules issued through the notice and comment process and do not apply to interpretative rules, general statements of policy, or rules of agency organization, procedure, or practice. Further, the requirements do not apply to a rule or major rule that relates to the management, organization, or personnel of an agency or procurement by the agency.</p><p>Any rule repealed under this bill must\u00a0be published in the Federal Register.</p><p>Finally, the Government Accountability Office must report on\u00a0the number and estimated cost of rules and major rules currently in effect.</p><p>\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119s30"
    },
    "title": "ERASER Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expediting Reform And Stopping Excess Regulations Act or the ERASER Act</strong></p><p>This bill generally requires federal agencies to repeal three rules before issuing a new rule.</p><p>In the case of a new nonmajor rule, an agency must repeal at least three rules that, to the extent practicable, are related to the new rule.</p><p>In the case of a new major rule, (1) an agency must repeal at least three rules\u00a0that are related to the new major rule, and (2) the cost of the new major rule must be less than or equal to the cost of the repealed rules.\u00a0A\u00a0<em>major rule</em> is a rule that has resulted in or is likely to result in (1) an annual effect on the economy of $100 million or more; (2) a major increase in costs or prices for consumers, individual industries, government agencies, or geographic regions; or (3) significant adverse effects on competition, employment, investment, productivity, or innovation.</p><p>These requirements apply to rules issued through the notice and comment process and do not apply to interpretative rules, general statements of policy, or rules of agency organization, procedure, or practice. Further, the requirements do not apply to a rule or major rule that relates to the management, organization, or personnel of an agency or procurement by the agency.</p><p>Any rule repealed under this bill must\u00a0be published in the Federal Register.</p><p>Finally, the Government Accountability Office must report on\u00a0the number and estimated cost of rules and major rules currently in effect.</p><p>\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119s30"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s30is.xml"
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
      "title": "ERASER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ERASER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expediting Reform And Stopping Excess Regulations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require each agency to repeal 3 existing regulations before issuing a new regulation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:35Z"
    }
  ]
}
```
