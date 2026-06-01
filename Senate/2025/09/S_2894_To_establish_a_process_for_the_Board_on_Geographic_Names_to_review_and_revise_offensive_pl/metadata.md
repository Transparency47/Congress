# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2894?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2894
- Title: Reconciliation in Place Names Act
- Congress: 119
- Bill type: S
- Bill number: 2894
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2894",
    "number": "2894",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Reconciliation in Place Names Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T20:35:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MN"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OR"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CO"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OR"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2894is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2894\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Ms. Warren (for herself, Mr. Booker , Ms. Duckworth , Mr. Padilla , Mr. Markey , Ms. Smith , Mr. Wyden , Mr. Hickenlooper , Mr. Merkley , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo establish a process for the Board on Geographic Names to review and revise offensive place names, to create an advisory committee to recommend offensive place names to be reviewed by the Board, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reconciliation in Place Names Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe United States contains geographic features named\u2014\n**(A)**\nwith derogatory terms that include racial and sexual slurs and stereotypes targeting Native Americans, African Americans, and others;\n**(B)**\nin honor of individuals who\u2014\n**(i)**\nheld racially repugnant views;\n**(ii)**\ncommitted atrocities against Native Americans; or\n**(iii)**\nsupported or effectuated discriminatory policies; and\n**(C)**\nto recognize individuals who carried out injustices against racial minorities;\n**(2)**\nplace names that include racial or sexual slurs, or honor individuals who held racially repugnant views, committed atrocities against Native Americans, or carried out injustices against racial minorities\u2014\n**(A)**\nperpetuate prejudice;\n**(B)**\ndisparage racial minorities; and\n**(C)**\nhonor individuals who committed or supported atrocities;\n**(3)**\nno geographic feature in the United States should have a name that\u2014\n**(A)**\nperpetuates prejudice;\n**(B)**\ndisparages racial minorities; or\n**(C)**\nhonors individuals who committed or supported atrocities against racial minorities;\n**(4)**\nplace names in the United States should\u2014\n**(A)**\nbe equitable and just;\n**(B)**\nhonor the cultural diversity of the United States; and\n**(C)**\nadvance dignity for all people in the United States;\n**(5)**\nthe Board on Geographic Names, jointly with the Secretary, is responsible for naming geographic features in the United States;\n**(6)**\nthe policies of the Board on Geographic Names\u2014\n**(A)**\nauthorize changing the names of geographic features determined to be offensive; and\n**(B)**\nprohibit the Federal use of terms determined to be derogatory or offensive in geographic place names;\n**(7)**\nthe renaming process of the Board on Geographic Names\u2014\n**(A)**\nis time consuming;\n**(B)**\nlacks transparency and public involvement; and\n**(C)**\nfails to address the scope and breadth of inappropriate place names;\n**(8)**\nthe extent of inappropriate or offensive place names in the United States requires a systematic, public process in which offensive and inappropriate place names are reviewed and replaced; and\n**(9)**\nthe process described in paragraph (8) offers an opportunity for reconciliation for\u2014\n**(A)**\npeople of the United States who suffer from prejudice and racial violence; and\n**(B)**\nall people of the United States in whose name the acts were committed.\n#### 3. Definitions\nIn this Act:\n**(1) Board**\nThe term Board means the Board on Geographic Names established by section 2 of the Act of July 25, 1947 ( 43 U.S.C. 364a ).\n**(2) Committee**\nThe term Committee means the Advisory Committee on Reconciliation in Place Names established by section 4(a).\n**(3) Federal land unit**\nThe term Federal land unit includes\u2014\n**(A)**\nNational Forest System land;\n**(B)**\na unit of the National Park System;\n**(C)**\na component of the National Wilderness Preservation System;\n**(D)**\nany part of the National Landscape Conservation System; and\n**(E)**\na unit of the National Wildlife Refuge System.\n**(4) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(5) Offensive place name**\nThe term offensive place name means a domestic geographic place name or Federal land unit name that\u2014\n**(A)**\nrecognizes an individual who\u2014\n**(i)**\n**(I)**\nheld racially repugnant views;\n**(II)**\ncommitted atrocities against Native Americans; or\n**(III)**\nsupported or effectuated discriminatory policies; or\n**(ii)**\ncarried out other injustices against racial minorities;\n**(B)**\ncontains a racial or sexual slur;\n**(C)**\nperpetuates racial, ethnic, or gender-based stereotypes; or\n**(D)**\nis derogatory or otherwise offensive.\n**(6) Tribal organization**\nThe term Tribal organization has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(7) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 4. Advisory committee\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish an advisory committee, to be known as the Advisory Committee on Reconciliation in Place Names .\n##### (b) Purpose\nThe purpose of the Committee is to advise the Board, the Secretary, and Congress with respect to renaming geographic features and Federal land units with offensive place names.\n##### (c) Membership\nThe Committee shall be composed of 17 members, to be appointed by the Secretary, of whom, to the extent practicable\u2014\n**(1)**\n4 members shall be members of an Indian Tribe;\n**(2)**\n1 member shall represent a Tribal organization;\n**(3)**\n1 member shall represent a Native Hawaiian organization;\n**(4)**\n4 members shall have a background in civil rights or race relations;\n**(5)**\n4 members shall have expertise in\u2014\n**(A)**\nanthropology;\n**(B)**\ncultural studies, ethnic studies, or indigenous studies;\n**(C)**\ngeography; or\n**(D)**\nhistory; and\n**(6)**\n3 members shall represent the general public.\n##### (d) Consultation with Indian Tribes\nBefore making an appointment under paragraph (1), (2), or (4) of subsection (c), the Secretary shall consult with Indian Tribes regarding the appointment.\n##### (e) Duties\nThe Committee shall\u2014\n**(1)**\nestablish a process to solicit and review proposals to rename geographic features and Federal land units with offensive place names;\n**(2)**\nsolicit proposals to rename geographic features and Federal land units with offensive place names and derogatory terms from\u2014\n**(A)**\nIndian Tribes;\n**(B)**\nappropriate State and local governments;\n**(C)**\nthe affected land management agency; and\n**(D)**\nmembers of the public;\n**(3)**\nprovide an opportunity for public comment on name change proposals;\n**(4)**\nmake proposals to the Board and the Secretary to rename geographic features with offensive place names, including proposed new names;\n**(5)**\nmake proposals to Congress to rename Federal land units with offensive place names, including proposed new names; and\n**(6)**\nmake recommendations to the Board on improvements to the process of reviewing and revising offensive place names.\n##### (f) Compensation\n**(1) In general**\nMembers of the Committee shall serve without compensation.\n**(2) Travel expenses**\nMembers of the Committee shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for an employee of an agency under subchapter I of chapter 57 of title 5, United States Code, while away from the home or regular place of business of the member in the performance of the duties of the Committee.\n##### (g) Staff\nThe Secretary shall provide the Committee with any staff members and technical assistance that the Secretary, after consultation with the Committee, determines to be appropriate to enable the Committee to carry out the duties of the Committee.\n##### (h) Rules\nThe Committee may adopt such rules as may be necessary.\n##### (i) Applicable law\nThe Committee shall be subject to chapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ).\n##### (j) Duration\n**(1) Timeline**\nTo the extent practicable, not later than 5 years after the date on which the Committee is established, the Committee shall fulfill the duties of the Committee, including the completion of the proposals required under paragraphs (4) and (5) of subsection (e).\n**(2) Termination**\nThe Committee shall terminate on the date that is 1 year after the date on which the Board has approved or rejected each Committee proposal submitted to the Board under subsection (e)(4).\n#### 5. Board review\n##### (a) In general\nNot later than 3 years after the date on which the Board receives a proposal under section 4(e)(4), the Board shall accept or reject the proposal.\n##### (b) Process\nThe Board shall approve a proposal of the Committee submitted under section 4(e)(4) unless the Board determines that\u2014\n**(1)**\nthere is a compelling reason and substantial public interest in rejecting the proposal; or\n**(2)**\napproving the proposal would violate Federal law.\n##### (c) Renaming\nIf the Board accepts a proposal by the Committee to rename a geographic feature, the Board shall rename the geographic feature.\n##### (d) Effect\nA Board policy that prevents the Board from considering a name change due to pending legislation shall not apply to Board action on Committee proposals.",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2843",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Reconciliation in Place Names Act",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-01T16:37:25Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2894is.xml"
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
      "title": "Reconciliation in Place Names Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reconciliation in Place Names Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a process for the Board on Geographic Names to review and revise offensive place names, to create an advisory committee to recommend offensive place names to be reviewed by the Board, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:23Z"
    }
  ]
}
```
