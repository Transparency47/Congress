# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3811?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3811
- Title: American Business for American Companies Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3811
- Origin chamber: Senate
- Introduced date: 2026-02-09
- Update date: 2026-04-23T14:46:21Z
- Update date including text: 2026-04-23T14:46:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in Senate
- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S535-537)
- Latest action: 2026-02-09: Introduced in Senate

## Actions

- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S535-537)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3811",
    "number": "3811",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "American Business for American Companies Act of 2026",
    "type": "S",
    "updateDate": "2026-04-23T14:46:21Z",
    "updateDateIncludingText": "2026-04-23T14:46:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S535-537)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T23:23:10Z",
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
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "RI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "IL"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-02-09",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3811is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3811\nIN THE SENATE OF THE UNITED STATES\nFebruary 9, 2026 Mr. Durbin (for himself, Mr. Reed , Ms. Duckworth , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit the award of Federal Government contracts to inverted domestic corporations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Business for American Companies Act of 2026 .\n#### 2. Prohibition on awarding contracts to inverted domestic corporations\n##### (a) Civilian contracts\n**(1) In general**\nChapter 47 of title 41, United States Code, is amended by adding at the end the following new section:\n4715. Prohibition on awarding contracts to inverted domestic corporations (a) Prohibition (1) In general The head of an executive agency may not award a contract for the procurement of property or services to\u2014 (A) any foreign incorporated entity that such head has determined is an inverted domestic corporation or any subsidiary of such entity; or (B) any joint venture if more than 10 percent of the joint venture (by vote or value) is held by a foreign incorporated entity that such head has determined is an inverted domestic corporation or any subsidiary of such entity. (2) Subcontracts (A) In general The head of an executive agency shall include in each contract for the procurement of property or services awarded by the executive agency with a value in excess of $10,000,000, other than a contract for exclusively commercial items, a clause that prohibits the prime contractor on such contract from\u2014 (i) awarding a first-tier subcontract with a value greater than 10 percent of the total value of the prime contract to an entity or joint venture described in paragraph (1); or (ii) structuring subcontract tiers in a manner designed to avoid the limitation in paragraph (1) by enabling an entity or joint venture described in paragraph (1) to perform more than 10 percent of the total value of the prime contract as a lower-tier subcontractor. (B) Penalties The contract clause included in contracts pursuant to subparagraph (A) shall provide that, in the event that the prime contractor violates the contract clause\u2014 (i) the prime contract may be terminated for default; and (ii) the matter may be referred to the suspension or debarment official for the appropriate agency and may be a basis for suspension or debarment of the prime contractor. (b) Inverted domestic corporation (1) In general For purposes of this section, a foreign incorporated entity shall be treated as an inverted domestic corporation if, pursuant to a plan (or a series of related transactions)\u2014 (A) the entity completes on or after May 8, 2014, the direct or indirect acquisition of\u2014 (i) substantially all of the properties held directly or indirectly by a domestic corporation; or (ii) substantially all of the assets of, or substantially all of the properties constituting a trade or business of, a domestic partnership; and (B) after the acquisition, either\u2014 (i) more than 50 percent of the stock (by vote or value) of the entity is held\u2014 (I) in the case of an acquisition with respect to a domestic corporation, by former shareholders of the domestic corporation by reason of holding stock in the domestic corporation; or (II) in the case of an acquisition with respect to a domestic partnership, by former partners of the domestic partnership by reason of holding a capital or profits interest in the domestic partnership; or (ii) the management and control of the expanded affiliated group which includes the entity occurs, directly or indirectly, primarily within the United States, as determined pursuant to regulations prescribed by the Secretary of the Treasury, and such expanded affiliated group has significant domestic business activities. (2) Exception for corporations with substantial business activities in foreign country of organization (A) In general A foreign incorporated entity described in paragraph (1) shall not be treated as an inverted domestic corporation if after the acquisition the expanded affiliated group which includes the entity has substantial business activities in the foreign country in which or under the law of which the entity is created or organized when compared to the total business activities of such expanded affiliated group. (B) Substantial business activities The Secretary of the Treasury (or the Secretary's delegate) shall establish regulations for determining whether an affiliated group has substantial business activities for purposes of subparagraph (A), except that such regulations may not treat any group as having substantial business activities if such group would not be considered to have substantial business activities under the regulations prescribed under section 7874 of the Internal Revenue Code of 1986, as in effect on January 18, 2017. (3) Significant domestic business activities (A) In general For purposes of paragraph (1)(B)(ii), an expanded affiliated group has significant domestic business activities if at least 25 percent of\u2014 (i) the employees of the group are based in the United States; (ii) the employee compensation incurred by the group is incurred with respect to employees based in the United States; (iii) the assets of the group are located in the United States; or (iv) the income of the group is derived in the United States. (B) Determination Determinations pursuant to subparagraph (A) shall be made in the same manner as such determinations are made for purposes of determining substantial business activities under regulations referred to in paragraph (2) as in effect on January 18, 2017, but applied by treating all references in such regulations to foreign country and relevant foreign country as references to the United States . The Secretary of the Treasury (or the Secretary's delegate) may issue regulations decreasing the threshold percent in any of the tests under such regulations for determining if business activities constitute significant domestic business activities for purposes of this paragraph. (c) Waiver (1) In general The head of an executive agency may waive subsection (a) with respect to any Federal Government contract under the authority of such head if the head determines that the waiver is\u2014 (A) required in the interest of national security; or (B) necessary for the efficient or effective administration of Federal or federally funded\u2014 (i) programs that provide health benefits to individuals; or (ii) public health programs. (2) Report to Congress The head of an executive agency issuing a waiver under paragraph (1) shall, not later than 14 days after issuing such waiver, submit a written notification of the waiver to the relevant authorizing committees of Congress and the Committees on Appropriations of the Senate and the House of Representatives. (d) Applicability (1) In general Except as provided in paragraph (2), this section shall not apply to any contract entered into before the date of the enactment of this section. (2) Task and delivery orders This section shall apply to any task or delivery order issued after the date of the enactment of this section pursuant to a contract entered into before, on, or after such date of enactment. (3) Scope This section applies only to contracts subject to regulation under the Federal Acquisition Regulation. (e) Definitions and special rules (1) Definitions In this section, the terms expanded affiliated group , foreign incorporated entity , person , domestic , and foreign have the meaning given those terms in section 835(c) of the Homeland Security Act of 2002 ( 6 U.S.C. 395(c) ). (2) Special rules In applying subsection (b) of this section for purposes of subsection (a) of this section, the rules described under 835(c)(1) of the Homeland Security Act of 2002 ( 6 U.S.C. 395(c)(1) ) shall apply. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 47 of title 41, United States Code, is amended by inserting after the item relating to section 4714 the following new item:\n4715. Prohibition on awarding contracts to inverted domestic corporations.\n##### (b) Defense contracts\n**(1) In general**\nChapter 363 of title 10, United States Code, is amended by adding at the end the following new section:\n4664. Prohibition on awarding contracts to inverted domestic corporations (a) Prohibition (1) In general The head of an agency may not award a contract for the procurement of property or services to\u2014 (A) any foreign incorporated entity that such head has determined is an inverted domestic corporation or any subsidiary of such entity; or (B) any joint venture if more than 10 percent of the joint venture (by vote or value) is owned by a foreign incorporated entity that such head has determined is an inverted domestic corporation or any subsidiary of such entity. (2) Subcontracts (A) In general The head of an executive agency shall include in each contract for the procurement of property or services awarded by the executive agency with a value in excess of $10,000,000, other than a contract for exclusively commercial items, a clause that prohibits the prime contractor on such contract from\u2014 (i) awarding a first-tier subcontract with a value greater than 10 percent of the total value of the prime contract to an entity or joint venture described in paragraph (1); or (ii) structuring subcontract tiers in a manner designed to avoid the limitation in paragraph (1) by enabling an entity or joint venture described in paragraph (1) to perform more than 10 percent of the total value of the prime contract as a lower-tier subcontractor. (B) Penalties The contract clause included in contracts pursuant to subparagraph (A) shall provide that, in the event that the prime contractor violates the contract clause\u2014 (i) the prime contract may be terminated for default; and (ii) the matter may be referred to the suspension or debarment official for the appropriate agency and may be a basis for suspension or debarment of the prime contractor. (b) Inverted domestic corporation (1) In general For purposes of this section, a foreign incorporated entity shall be treated as an inverted domestic corporation if, pursuant to a plan (or a series of related transactions)\u2014 (A) the entity completes on or after May 8, 2014, the direct or indirect acquisition of\u2014 (i) substantially all of the properties held directly or indirectly by a domestic corporation; or (ii) substantially all of the assets of, or substantially all of the properties constituting a trade or business of, a domestic partnership; and (B) after the acquisition, either\u2014 (i) more than 50 percent of the stock (by vote or value) of the entity is held\u2014 (I) in the case of an acquisition with respect to a domestic corporation, by former shareholders of the domestic corporation by reason of holding stock in the domestic corporation; or (II) in the case of an acquisition with respect to a domestic partnership, by former partners of the domestic partnership by reason of holding a capital or profits interest in the domestic partnership; or (ii) the management and control of the expanded affiliated group which includes the entity occurs, directly or indirectly, primarily within the United States, as determined pursuant to regulations prescribed by the Secretary of the Treasury, and such expanded affiliated group has significant domestic business activities. (2) Exception for corporations with substantial business activities in foreign country of organization (A) In general A foreign incorporated entity described in paragraph (1) shall not be treated as an inverted domestic corporation if after the acquisition the expanded affiliated group which includes the entity has substantial business activities in the foreign country in which or under the law of which the entity is created or organized when compared to the total business activities of such expanded affiliated group. (B) Substantial business activities The Secretary of the Treasury (or the Secretary's delegate) shall establish regulations for determining whether an affiliated group has substantial business activities for purposes of subparagraph (A), except that such regulations may not treat any group as having substantial business activities if such group would not be considered to have substantial business activities under the regulations prescribed under section 7874 of the Internal Revenue Code of 1986, as in effect on January 18, 2017. (3) Significant domestic business activities (A) In general For purposes of paragraph (1)(B)(ii), an expanded affiliated group has significant domestic business activities if at least 25 percent of\u2014 (i) the employees of the group are based in the United States; (ii) the employee compensation incurred by the group is incurred with respect to employees based in the United States; (iii) the assets of the group are located in the United States; or (iv) the income of the group is derived in the United States. (B) Determination Determinations pursuant to subparagraph (A) shall be made in the same manner as such determinations are made for purposes of determining substantial business activities under regulations referred to in paragraph (2) as in effect on January 18, 2017, but applied by treating all references in such regulations to foreign country and relevant foreign country as references to the United States . The Secretary of the Treasury (or the Secretary's delegate) may issue regulations decreasing the threshold percent in any of the tests under such regulations for determining if business activities constitute significant domestic business activities for purposes of this paragraph. (c) Waiver (1) In general The head of an agency may waive subsection (a) with respect to any Federal Government contract under the authority of such head if the head determines that the waiver is required in the interest of national security or is necessary for the efficient or effective administration of Federal or federally funded programs that provide health benefits to individuals. (2) Report to Congress The head of an agency issuing a waiver under paragraph (1) shall, not later than 14 days after issuing such waiver, submit a written notification of the waiver to the congressional defense committees. (d) Applicability (1) In general Except as provided in paragraph (2), this section shall not apply to any contract entered into before the date of the enactment of this section. (2) Task and delivery orders This section shall apply to any task or delivery order issued after the date of the enactment of this section pursuant to a contract entered into before, on, or after such date of enactment. (3) Scope This section applies only to contracts subject to regulation under the Federal Acquisition Regulation and the Defense Supplement to the Federal Acquisition Regulation. (e) Definitions and special rules (1) Definitions In this section, the terms expanded affiliated group , foreign incorporated entity , person , domestic , and foreign have the meaning given those terms in section 835(c) of the Homeland Security Act of 2002 ( 6 U.S.C. 395(c) ). (2) Special rules In applying subsection (b) of this section for purposes of subsection (a) of this section, the rules described under 835(c)(1) of the Homeland Security Act of 2002 ( 6 U.S.C. 395(c)(1) ) shall apply. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 363 of title 10, United States Code, is amended by inserting after the item relating to section 4663 the following new item:\n4664. Prohibition on awarding contracts to inverted domestic corporations.\n##### (c) Regulations regarding management and control\n**(1) In general**\nThe Secretary of the Treasury (or the Secretary's delegate) shall, for purposes of section 4715(b)(1)(B)(ii) of title 41, United States Code, and section 4664(b)(1)(B)(ii) of title 10, United States Code, as added by subsections (a) and (b), respectively, prescribe regulations for purposes of determining cases in which the management and control of an expanded affiliated group is to be treated as occurring, directly or indirectly, primarily within the United States. The regulations prescribed under the preceding sentence shall apply to periods after May 8, 2014.\n**(2) Executive officers and senior management**\nThe regulations prescribed under paragraph (1) shall provide that the management and control of an expanded affiliated group shall be treated as occurring, directly or indirectly, primarily within the United States if substantially all of the executive officers and senior management of the expanded affiliated group who exercise day-to-day responsibility for making decisions involving strategic, financial, and operational policies of the expanded affiliated group are based or primarily located within the United States. Individuals who in fact exercise such day-to-day responsibilities shall be treated as executive officers and senior management regardless of their title.",
      "versionDate": "2026-02-09",
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
        "actionDate": "2026-02-09",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7424",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "American Business for American Companies Act of 2026",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-27T16:44:21Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3811is.xml"
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
      "title": "American Business for American Companies Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Business for American Companies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the award of Federal Government contracts to inverted domestic corporations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T03:48:24Z"
    }
  ]
}
```
