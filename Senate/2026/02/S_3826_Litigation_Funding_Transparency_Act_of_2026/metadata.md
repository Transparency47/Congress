# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3826?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3826
- Title: Litigation Funding Transparency Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3826
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-02-27T17:57:47Z
- Update date including text: 2026-02-27T17:57:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-11: Introduced in Senate

## Actions

- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3826",
    "number": "3826",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Litigation Funding Transparency Act of 2026",
    "type": "S",
    "updateDate": "2026-02-27T17:57:47Z",
    "updateDateIncludingText": "2026-02-27T17:57:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T19:15:33Z",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "NC"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "LA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3826is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3826\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Mr. Grassley (for himself, Mr. Tillis , Mr. Kennedy , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to increase transparency and oversight of third-party litigation funding in certain actions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Litigation Funding Transparency Act of 2026 .\n#### 2. Transparency and oversight of third-party litigation funding in class and mass actions\n##### (a) In general\nChapter 115 of title 28, United States Code, is amended by adding at the end the following:\n1747. Third-party litigation funding disclosure (a) Definitions In this section: (1) Class action The term class action has the meaning given the term in section 1711. (2) Commercial enterprise The term commercial enterprise \u2014 (A) means any entity formed for the ongoing conduct of lawful business; and (B) does not include any entity that, in a covered civil action, has a right or expectation of payment based on any activity, right, or interest described in subparagraph (A) or (B) of paragraph (8) that is limited to\u2014 (i) the repayment of the principal of a loan; (ii) the repayment of the principal of a loan plus interest that does not exceed the greater of 10 percent or a rate 3 times the annual average 30-year constant maturity Treasury yield, as published by the Board of Governors of the Federal Reserve System, for the year preceding the date on which the relevant agreement was executed; or (iii) the reimbursement of fees or grants paid or given to counsel of record for services provided in a covered civil action. (3) Covered civil action The term covered civil action \u2014 (A) means\u2014 (i) any civil action transferred to or filed in coordinated or consolidated pretrial proceedings established by the judicial panel on multidistrict litigation pursuant to section 1407; (ii) any class action; and (iii) any civil action filed in a coordinated or consolidated proceeding before a district court of the United States that includes not fewer than 100 civil actions; and (B) does not include any action brought or funded by a nonprofit legal organization funded by donors that is providing funding or representation to clients on a pro bono basis if the donations to the nonprofit organization that are used to bring or fund the action were not provided by a foreign state, a foreign person, a sovereign wealth fund, or a commercial enterprise, any of which is controlled by or owned by a foreign state, foreign person, or sovereign wealth fund. (4) Foreign person The term foreign person \u2014 (A) means any person that is not a United States person; and (B) does not include a foreign state or a sovereign wealth fund. (5) Foreign principal The term foreign principal has the meaning given the term in section 1 of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 611 ). (6) Foreign state The term foreign state has the meaning given the term in section 1603. (7) Sovereign wealth fund The term sovereign wealth fund means an investment fund owned or controlled by a foreign state, an agency or instrumentality of a foreign state, or an entity a majority of the shares or other ownership interest of which is owned or controlled by a foreign state or by an agency or instrumentality of a foreign state. (8) Third-party funder The term third-party funder means any commercial enterprise, foreign state, foreign person, or sovereign wealth fund, other than counsel of record, that\u2014 (A) provides or agrees to provide direct or indirect monetary support to a party, counsel, or law firm for purposes of funding the initiation or litigation of a covered civil action in which neither the commercial enterprise, foreign state, foreign person, or sovereign wealth fund, as applicable, nor a subsidiary corporation thereof (as defined in section 424(f) of the Internal Revenue Code of 1986, determined by substituting corporation which is the commercial enterprise, foreign state, foreign person, or sovereign wealth fund described in section 1747(a)(8) of title 28, United States Code, for employer corporation each place it appears), is a named party; or (B) as a nonparty, has a right to receive in return anything that is greater in value than what is given or granted that is related in any respect to proceeds from a covered civil action or a group of actions of which the covered civil action is a part, by settlement, judgment, attorney's fees, or otherwise. (9) United States person The term United States person has the meaning given the term in section 101 of the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 ). (b) Disclosure In any covered civil action, a party or any counsel of record for a party shall\u2014 (1) disclose in writing to the court and all other named parties to the action the identity of any third-party funder of the action; (2) disclose in writing to the court and all other named parties to the action whether any third-party funder of the action is a foreign state, foreign person, sovereign wealth fund, or a commercial enterprise that is directly or indirectly controlled by or owned by a foreign state, foreign person, or a sovereign wealth fund; (3) produce for inspection and copying to the court and to all other named parties to the action any agreement concerning the provision of monetary support described in subsection (a)(8)(A) or creating the right described in subsection (a)(8)(B), unless otherwise ordered by the court; and (4) transmit to the Administrative Office of the United States Courts copies of any disclosures made under paragraph (2), or any productions made under paragraph (3) in any case in which a disclosure is required under paragraph (2). (c) Timing The disclosures and notifications required by subsection (b) shall be made not later than the later of\u2014 (1) 10 days after the execution of any agreement described in subsection (b)(3); or (2) the time of service of the action. (d) Duty To correct A party or counsel of record that made a disclosure required by this section shall supplement or correct each such disclosure in a timely manner\u2014 (1) if such party or counsel of record learns that the disclosure is or has become incomplete or incorrect in some material respect, if the additional or corrective information has not otherwise been made known to the other parties during the discovery process or in writing; or (2) as ordered by the court. (e) Enforcement The obligations set forth in subsection (b) shall be deemed to be disclosures required by rule 26(a) of the Federal Rules of Civil Procedure and shall be subject to the sanction provisions of rule 37 of the Federal Rules of Civil Procedure. (f) Website update; report Not later than 180 days after the date of enactment of this section, and every 120 days thereafter, the Administrative Office of the United States Courts shall submit to Congress, the Attorney General, and the Principal Deputy Assistant Attorney General for National Security and shall post on the United States Courts website a report that lists\u2014 (1) each foreign state, foreign person, sovereign wealth fund, or commercial enterprise that was identified in a covered civil action in response to subsection (b)(2) or subsection (g) during the preceding 120 days; (2) the caption and docket number of the action described in paragraph (1); (3) the court in which the action described in paragraph (1) is pending; (4) the amount of any monetary support provided by the person identified in paragraph (1); and (5) the total amount each foreign state, foreign person, sovereign wealth fund, or commercial enterprise listed in paragraph (1) has provided in support of any covered civil action during the preceding 120 days. (g) Litigation integrity (1) In general No third-party funder in a covered civil action shall exert or be afforded the right to exert, by contract or otherwise, influence, control, or discretion regarding the litigation strategy, decision-making, or settlement negotiations of a party. (2) Contempt The court presiding over a covered civil action may\u2014 (A) hold in contempt any person that violates paragraph (1); and (B) for purposes of issuing and enforcing a contempt order under subparagraph (A), exercise the powers of a district judge in any district. (h) Protection of proprietary information acquired during the discovery process (1) In general In a covered civil action, no third-party funder or any agent, counsel, or representative of a third-party funder may obtain, inspect, copy, or otherwise view any discovery materials that are produced in the action subject to a protective order issued pursuant to rule 26(c)(1)(G) of the Federal Rules of Civil Procedure, unless specifically authorized by the court. (2) Contempt The court presiding over a covered civil action may\u2014 (A) hold in contempt any person or entity that violates paragraph (1); and (B) for purposes of issuing and enforcing a contempt order under subparagraph (A), exercise the powers of a district court in any district. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 115 of title 28, United States Code, is amended by adding at the end the following:\n1747. Third-party litigation funding disclosure. .\n#### 3. Applicability\nThe amendments made by this Act shall apply to any case pending on or commenced after the date of enactment of this Act.",
      "versionDate": "2026-02-11",
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
        "name": "Law",
        "updateDate": "2026-02-27T17:57:47Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3826is.xml"
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
      "title": "Litigation Funding Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Litigation Funding Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 28, United States Code, to increase transparency and oversight of third-party litigation funding in certain actions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T04:48:24Z"
    }
  ]
}
```
