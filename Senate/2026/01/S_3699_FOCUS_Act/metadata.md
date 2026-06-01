# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3699?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3699
- Title: FOCUS Act
- Congress: 119
- Bill type: S
- Bill number: 3699
- Origin chamber: Senate
- Introduced date: 2026-01-27
- Update date: 2026-02-25T16:25:49Z
- Update date including text: 2026-02-25T16:25:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in Senate
- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-27: Introduced in Senate

## Actions

- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3699",
    "number": "3699",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "FOCUS Act",
    "type": "S",
    "updateDate": "2026-02-25T16:25:49Z",
    "updateDateIncludingText": "2026-02-25T16:25:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T22:10:35Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MN"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3699is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3699\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Mr. Booker (for himself, Ms. Klobuchar , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 287 of the Immigration and Nationality Act to require all Federal law enforcement officers engaged in or supporting immigration enforcement or related enforcement activities to wear and operate a body camera while on duty to ensure transparency and accountability.\n#### 1. Short titles\nThis Act may be cited as the Federal Officers Camera Use for Safety Act or the FOCUS Act .\n#### 2. Body camera usage\nSection 287 of the Immigration and Nationality Act ( 8 U.S.C. 1357 ) is amended\u2014\n**(1)**\nby striking Service each place such term appears and inserting Department of Homeland Security ;\n**(2)**\nby striking Attorney General each place such term appears and inserting Secretary of Homeland Security ;\n**(3)**\nin subsection (h)\u2014\n**(A)**\nby striking of the Immigration and Nationality Act ; and\n**(B)**\nby striking of such Act ; and\n**(4)**\nby adding at the end the following:\n(i) Body camera usage (1) Definitions In this subsection: (A) Body worn camera The term body worn camera means a mobile audio and video recording system worn by a law enforcement officer. (B) Federal law enforcement officer The term Federal law enforcement officer \u2014 (i) means any officer, agent, or employee of the United States Government that is authorized by law or by a Government agency to engage in or supervise the prevention, detection, or investigation of any violation of Federal civil or criminal law; and (ii) includes individuals employed by private contractors who are so authorized to carry out the functions described in clause (i). (2) In general Each Federal law enforcement officer shall wear and operate a body worn camera while engaged in or supporting immigration enforcement or related enforcement activities. (3) Use of footage Except as provided in paragraph (4), video footage from a body worn camera operated pursuant to paragraph (2)\u2014 (A) shall be retained for 1 year after the date on which such footage was recorded by the agency that employed the Federal law enforcement officer that was wearing the body worn camera; and (B) may be permanently deleted after the period described in subparagraph (A) unless such footage captured\u2014 (i) images involving any use of force; (ii) events preceding and including an arrest or detention for a crime or attempted crime; or (iii) an encounter about which a complaint has been registered by a subject of the video footage. (4) Extended retention period Video footage from a body worn camera operated pursuant to paragraph (2) shall be retained for not less than 3 years after the date on which such footage was recorded if a longer retention period is voluntarily requested by\u2014 (A) the Federal law enforcement officer whose body worn camera recorded the video footage, if such officer reasonably asserts the video footage has evidentiary or exculpatory value; (B) a Federal law enforcement officer who is a subject of the video footage, if such officer reasonably asserts the video footage has evidentiary or exculpatory value; (C) any supervisor of an officer whose body worn camera recorded the video footage or who is a subject of the video footage, if such supervisor reasonably asserts the video footage has evidentiary or exculpatory value; (D) a Federal law enforcement officer, if the video footage is being retained solely and exclusively for training purposes; (E) a member of the public who is a subject of the video footage, or such individual's legal representative; (F) a parent or legal guardian of a minor who is a subject of the video footage; or (G) a deceased subject's next of kin or legally authorized designee. (5) Access to footage All video footage of any interaction or event captured by a body camera that is requested by a person or entity and identified with reasonable specificity shall be provided to such person or entity in accordance with the procedures for requesting and providing government records set forth in section 552 of title 5, United States Code. (6) Body worn camera accountability requirements All body worn cameras shall be equipped with\u2014 (A) automatic camera activation; (B) audit trail logging; (C) GPS-based location services; and (D) LTE wireless evidence upload. .\n#### 3. Compliance and reporting\n##### (a) Defined term\nIn this section, the term Federal law enforcement officer \u2014\n**(1)**\nmeans any officer, agent, or employee of the United States Government authorized by law or by a Government agency to engage in or supervise the prevention, detection, or investigation of any violation of Federal civil or criminal law; and\n**(2)**\nincludes individuals employed by private contractors who are so authorized to carry out the functions described in paragraph (1).\n##### (b) Internal accountability\nAny Federal law enforcement officer who fails to comply with the requirements under section 287(i) of the Immigration and Nationality Act, as added by section 2 shall be\u2014\n**(1)**\nrequired to review the body worn camera policy of the agency employing such officer; and\n**(2)**\nsubject to appropriate administrative discipline, including written reprimand, suspension, or other personnel actions, consistent with agency policy and any applicable collective bargaining agreement.\n##### (c) Documentation\nEach violation of section 287(i) of the Immigration and Nationality Act, as added by section 2, caused by a device malfunction, operator error, or other circumstances, shall be documented in a report that\u2014\n**(1)**\nis submitted by the Federal law enforcement officer involved in such violation to his or her supervisor; and\n**(2)**\nincludes, as applicable, a description of the reason the recording was not made, was interrupted, or was terminated.\n##### (d) Misconduct\nAny Federal law enforcement officer who intentionally turns off the body worn camera in violation of section 287(i) of the Immigration and Nationality Act, as added by section 2, shall be subject to discipline, which may include termination of employment.\n##### (e) Supervisory responsibilities\nEach supervisor of Federal law enforcement officers shall ensure that such officers receive the required training regarding the use of body worn cameras in accordance with the policies described in section 287(i) of the Immigration and Nationality Act and this Act.\n##### (f) Annual report to Congress\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter, the Secretary of Homeland Security shall submit an unredacted report to the Office for Civil Rights and Civil Liberties, the Committee on the Judiciary of the Senate , the Committee on Homeland Security and Governmental Affairs of the Senate , the Committee on the Judiciary of the House of Representatives , and the Committee on Homeland Security of the House of Representatives that includes\u2014\n**(1)**\nthe number of documented violations of section 287(i) of the Immigration and Nationality Act, as added by section 2; and\n**(2)**\na summary of disciplinary or remedial actions taken against Federal law enforcement officers responsible for such violations.\n##### (g) Public availability\n**(1) In general**\nSubject to paragraph (2), not later than 30 days after each annual report is submitted to Congress pursuant to subsection (f)\u2014\n**(A)**\nthe Secretary of Homeland Security shall post a copy of the report on a publicly accessible website of the Department of Homeland Security; and\n**(B)**\nthe congressional committees referred to in subsection (f) shall post a copy of the report on their respective websites.\n**(2) Redactions to publicly available report**\nThe Inspector General of the Department of Homeland Security may redact information from the public version of such report if\u2014\n**(A)**\nsuch redactions are necessary to protect sensitive law enforcement operations, ongoing investigations, or individual privacy; and\n**(B)**\nthe justification for such redactions is included in the report.\n##### (h) Independent review panel\nThe Secretary of Homeland Security shall establish an independent advisory panel composed of experts in civil rights, privacy, technology, and law enforcement oversight to provide recommendations regarding policies governing the use and management of body worn cameras and recorded footage.",
      "versionDate": "2026-01-27",
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
        "updateDate": "2026-02-25T16:25:49Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3699is.xml"
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
      "title": "FOCUS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FOCUS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Officers Camera Use for Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 287 of the Immigration and Nationality Act to require all Federal law enforcement officers engaged in or supporting immigration enforcement or related enforcement activities to wear and operate a body camera while on duty to ensure transparency and accountability.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:29Z"
    }
  ]
}
```
