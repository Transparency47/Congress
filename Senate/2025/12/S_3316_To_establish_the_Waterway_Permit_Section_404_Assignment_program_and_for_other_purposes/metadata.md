# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3316?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3316
- Title: WATER Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3316
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-01-07T16:50:58Z
- Update date including text: 2026-01-07T16:50:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3316",
    "number": "3316",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "WATER Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T16:50:58Z",
    "updateDateIncludingText": "2026-01-07T16:50:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:50:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3316is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3316\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mr. Husted (for himself and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo establish the Waterway Permit Section 404 Assignment program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Water Authority and Timely Environmental Review Act of 2025 or the WATER Act of 2025 .\n#### 2. Waterway Permit Section 404 Assignment program\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Covered project**\nThe term covered project means a highway, railroad, or public transportation project.\n**(3) FWPCA terms**\nThe terms navigable waters and State have the meanings given those terms in section 502 of the Federal Water Pollution Control Act ( 33 U.S.C. 1362 ).\n**(4) Program**\nThe term program means the Waterway Permit Section 404 Assignment program established under subsection (b)(1).\n**(5) Secretary**\nThe term Secretary means the Secretary of the Army, acting through the Chief of Engineers.\n##### (b) Establishment\n**(1) In general**\nNot later than 60 days after the date of enactment of this Act, the Secretary and the Administrator shall jointly establish and carry out a program, to be known as the Waterway Permit Section 404 Assignment program .\n**(2) Assumption of responsibility**\n**(A) In general**\nSubject to the requirements of this section and notwithstanding subsections (g) through (m) of section 404 of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ), with the written agreement of the Secretary, the Administrator, and a State, which may be in the form of a memorandum of understanding, the Secretary may assign, and the State may assume, the responsibilities of the Secretary under that section with respect to the permitting of 1 or more covered projects in the State.\n**(B) Additional responsibility**\nIf a State assumes responsibility under subparagraph (A)\u2014\n**(i)**\nthe Secretary may assign to the State, and the State may assume, all or part of the responsibilities of the Secretary for the permitting of discharge of dredged or fill material into the navigable waters, including environmental reviews under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), consultation requirements under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), requirements under division A of subtitle III of title 54, United States Code, or any other action required under any Federal environmental law relating to review under section 404 of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ) or approval of a covered project; and\n**(ii)**\nsubject to subparagraph (C), the Secretary may assign to the State, and the State may assume, all or part of the responsibilities of the Secretary under section 10 of the Act of March 3, 1899 (commonly known as the Rivers and Harbors Act of 1899 ) (30 Stat. 1151, chapter 425; 33 U.S.C. 403 ), for the permitting of the construction of any structure in or over any navigable water of the United States, the excavating from or depositing of material in such waters, or the accomplishment of any other work affecting the course, location, condition, or capacity of such waters.\n**(C) Limitations with respect to rivers and harbors act of 1899**\nThe assignment of responsibilities under subparagraph (B)(ii) shall be limited to the program and is effective only as it is necessary to allow for the permitting of a covered project.\n**(D) Procedural and substantive requirements**\n**(i) In general**\nExcept as otherwise provided in this section\u2014\n**(I)**\na State shall assume responsibility under this section subject to the same procedural and substantive requirements as would apply if that responsibility were carried out by the Secretary; and\n**(II)**\nthe State shall ensure compliance with those requirements.\n**(ii) No regulations required**\nNothing in this section requires a State participating in the program to promulgate regulations to carry out the program.\n**(E) Federal responsibility**\n**(i) In general**\nAny responsibility of the Secretary under section 404 of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ) or section 10 of the Act of March 3, 1899 (commonly known as the Rivers and Harbors Act of 1899 ) (30 Stat. 1151, chapter 425; 33 U.S.C. 403 ), not explicitly assumed by a State by written agreement under this section shall remain the responsibility of the Secretary.\n**(ii) Savings provision**\nNothing in this section requires the Secretary to assign to a State, or that State to accept, any of the enforcement authority of the Secretary under section 404(s) of the Federal Water Pollution Control Act ( 33 U.S.C. 1344(s) ).\n**(F) No effect on authority**\nNothing in this section preempts or interferes with any power, jurisdiction, responsibility, or authority of a Federal agency, other than the Environmental Protection Agency and the Corps of Engineers, under applicable law (including regulations) with respect to a covered project.\n**(G) Preservation of flexibility**\nThe Secretary may not require a State, as a condition of participation in the program, to forego project delivery methods that are otherwise permissible for covered projects.\n**(H) Legal fees**\nA State assuming the responsibilities of the Secretary under the program for a specific covered project may use funds apportioned to the State under section 104(b)(2) of title 23, United States Code, for attorneys' fees directly attributable to eligible activities associated with the covered project, including the payment of fees awarded under section 2412 of title 28, United States Code.\n##### (c) State Participation\n**(1) Participating States**\nAll States are eligible to participate in the program.\n**(2) Application**\nNot later than 270 days after the date of enactment of this Act, the Secretary may promulgate or amend, as appropriate, regulations or issue guidance that establishes requirements relating to information required to be contained in any application of a State to participate in the program, including, at a minimum\u2014\n**(A)**\nthe covered projects or classes of covered projects for which the State anticipates exercising the authority that may be granted under the program;\n**(B)**\na demonstration of the ability of the State to assure consistency with guidelines established under section 404(b)(1) of the Federal Water Pollution Control Act ( 33 U.S.C. 1344(b)(1) );\n**(C)**\nverification of the financial resources necessary to carry out the authority that may be granted under the program; and\n**(D)**\nevidence of the notice and solicitation of public comment by the State relating to participation of the State in the program, including copies of comments received from that solicitation.\n**(3) Public notice**\n**(A) In general**\nNot later than 30 days before the date on which a State submits an application under this subsection, the State shall give notice of the intent of the State to participate in the program, in accordance with subparagraph (B).\n**(B) Method of notice and solicitation**\nThe State shall provide notice and solicit public comment under subparagraph (A) by publishing the complete application of the State in accordance with the appropriate public notice law of the State.\n**(4) Selection criteria**\nThe Secretary may approve the application of a State under this subsection only if\u2014\n**(A)**\nthe requirements under paragraph (2) have been met;\n**(B)**\nthe Secretary determines that the State has the capability, including financial and personnel, to assume responsibility under the program; and\n**(C)**\nthe head of the State agency having primary jurisdiction over highway matters enters into a written agreement described in subsection (d) with the Secretary.\n**(5) Other Federal agency views**\nIf a State applies to assume a responsibility of the Secretary that would have required the Secretary to consult with another Federal agency, the Secretary shall solicit the views of the Federal agency before approving the application.\n##### (d) Written Agreement\n**(1) In general**\nA written agreement under this section shall\u2014\n**(A)**\nbe executed by the Governor or the top-ranking transportation official in the State who is charged with responsibility for transportation infrastructure operation, maintenance, and construction;\n**(B)**\nbe in such form as the Secretary may prescribe;\n**(C)**\nprovide that the State\u2014\n**(i)**\nagrees to assume all or part of the responsibilities of the Secretary described in subsection (b)(2);\n**(ii)**\nexpressly consents, on behalf of the State, to accept the jurisdiction of the Federal courts for the compliance, discharge, and enforcement of any responsibility of the Secretary assumed by the State;\n**(iii)**\ncertifies that State laws are in effect that\u2014\n**(I)**\nauthorize the State to take the actions necessary to carry out the responsibilities being assumed; and\n**(II)**\nare comparable to section 552 of title 5, United States Code, including providing that any decision relating to the public availability of a document under those State laws is reviewable by a court of competent jurisdiction; and\n**(iv)**\nagrees to maintain the financial resources necessary to carry out the responsibilities being assumed;\n**(D)**\nrequire the State to provide to the Secretary any information the Secretary reasonably considers necessary to ensure that the State is adequately carrying out the responsibilities assigned to the State;\n**(E)**\n**(i)**\nhave a term of not more than 5 years; or\n**(ii)**\nin the case of a State that has participated in a program under section 326 or 327 of title 23, United States Code, for a period of not less than 10 years, have a term of 10 years; and\n**(F)**\nbe renewable.\n**(2) No additional requirements**\nThe Secretary may not include any additional requirements in a written agreement under this section other than the requirements described in paragraph (1).\n##### (e) Jurisdiction\n**(1) In general**\nThe district courts of the United States shall have exclusive jurisdiction over any civil action against a State for failure to carry out any responsibility of the State under the program.\n**(2) Legal standards and requirements**\nA civil action described in paragraph (1) shall be governed by the legal standards and requirements that would apply in such a civil action against the Secretary had the Secretary taken the actions in question.\n**(3) Intervention**\nThe Secretary shall have the right to intervene in any civil action described in paragraph (1).\n##### (f) Effect of Assumption of Responsibility\nA State that assumes responsibility under subsection (b)(2) shall be solely responsible and solely liable for carrying out, in lieu of and without further approval of the Secretary, the responsibilities assumed under that subsection, until the program is terminated under subsection (k).\n##### (g) Limitations on Agreements\nNothing in this section permits a State to assume any rulemaking authority of the Secretary under any Federal law.\n##### (h) Audits\n**(1) In general**\nTo ensure compliance by a State with any agreement of the State under subsection (d) (including compliance by the State with all Federal laws for which responsibility is assumed under subsection (b)(2)), for each State participating in the program under this section, the Secretary shall\u2014\n**(A)**\nnot later than 180 days after the date of execution of the agreement, meet with the State to review implementation of the agreement and discuss plans for the first annual audit;\n**(B)**\nconduct not more than 2 audits during the first 4 years that the State is participating in the program;\n**(C)**\nin the case of an agreement period of greater than 5 years pursuant to subsection (d)(1)(E)(ii), conduct an audit covering the first 5 years of the agreement period and a second audit covering the final 5 years of the agreement; and\n**(D)**\nensure that the time period for completing an audit, from initiation to completion (including public comment and responses to those comments), does not exceed 180 days.\n**(2) Public availability and comment**\n**(A) In general**\nAn audit conducted under paragraph (1) shall be provided to the public for comment.\n**(B) Response**\nNot later than 60 days after the date on which the period for public comment described in subparagraph (A) ends, the Secretary shall respond to public comments received under that subparagraph.\n**(3) Audit team**\n**(A) In general**\nAn audit conducted under paragraph (1) shall be carried out by an audit team determined by the Secretary, in consultation with the State, in accordance with subparagraph (B).\n**(B) Consultation**\nConsultation with the State under subparagraph (A) shall include a reasonable opportunity for the State to review and provide comments on the proposed members of the audit team.\n##### (i) Monitoring\nAfter the fourth year of the participation of a State in the program, the Secretary shall monitor compliance by the State with the written agreement, including the provision by the State of financial resources to carry out the written agreement.\n##### (j) Reports to Congress\nThe Secretary shall submit to Congress an annual report that describes the administration of the program.\n##### (k) Termination\n**(1) Termination by Secretary**\nThe Secretary may terminate the participation of any State in the program if\u2014\n**(A)**\nthe Secretary determines that the State is not adequately carrying out the responsibilities assigned to the State;\n**(B)**\nthe Secretary provides to the State\u2014\n**(i)**\na notification of the determination of noncompliance;\n**(ii)**\na period of not less than 120 days to take such corrective action as the Secretary determines to be necessary to comply with the applicable agreement; and\n**(iii)**\non request of the Governor of the State, a detailed description of each responsibility in need of corrective action regarding an inadequacy identified under subparagraph (A); and\n**(C)**\nthe State, after the notification and period provided under subparagraph (B), fails to take satisfactory corrective action, as determined by the Secretary.\n**(2) Termination by the State**\nThe State may terminate the participation of the State in the program at any time by providing to the Secretary a notice by not later than the date that is 90 days before the date of termination, subject to such terms and conditions as the Secretary may provide.\n##### (l) Capacity Building\nThe Secretary, in cooperation with representatives of State officials, may carry out education, training, peer-exchange, and other initiatives, as appropriate\u2014\n**(1)**\nto assist States in developing the capacity to participate in the program; and\n**(2)**\nto promote information sharing and collaboration among States that are participating in the program.\n##### (m) Relationship to Locally Administered Projects\nA State granted authority under this section may, in its sole discretion on the request of a unit of local government in the State\u2014\n**(1)**\nexercise such authority on behalf of the unit of local government for a locally administered project; or\n**(2)**\nprovide guidance and training on consolidating and minimizing the documentation and environmental analyses necessary for sponsors of a locally administered project to comply with the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) and any comparable requirements under State law.\n##### (n) Agency Deemed To Be Federal Agency\nA State agency that is assigned a responsibility under an agreement under this section shall be deemed to be an agency for the purposes of section 2412 of title 28, United States Code.",
      "versionDate": "2025-12-03",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-07T16:50:58Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3316is.xml"
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
      "title": "WATER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WATER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Water Authority and Timely Environmental Review Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Waterway Permit Section 404 Assignment program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:33:14Z"
    }
  ]
}
```
