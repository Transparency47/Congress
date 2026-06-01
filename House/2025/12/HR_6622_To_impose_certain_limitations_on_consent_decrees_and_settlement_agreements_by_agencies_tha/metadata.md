# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6622?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6622
- Title: Sunshine for Regulatory Decrees and Settlements Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6622
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-01-09T09:06:50Z
- Update date including text: 2026-01-09T09:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-08 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-08 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 18 - 8.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-08 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-08 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 18 - 8.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6622",
    "number": "6622",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Sunshine for Regulatory Decrees and Settlements Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:50Z",
    "updateDateIncludingText": "2026-01-09T09:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 18 - 8.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
        "item": [
          {
            "date": "2026-01-08T20:43:30Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-11T16:04:50Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6622ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6622\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Cline (for himself and Mr. Tiffany ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo impose certain limitations on consent decrees and settlement agreements by agencies that require the agencies to take regulatory action in accordance with the terms thereof, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sunshine for Regulatory Decrees and Settlements Act of 2025 .\n#### 2. Definitions\nIn this Act\u2014\n**(1)**\nthe terms agency and agency action have the meanings given those terms under section 551 of title 5, United States Code;\n**(2)**\nthe term covered civil action means a civil action\u2014\n**(A)**\nseeking to compel agency action;\n**(B)**\nalleging that an agency is unlawfully withholding or unreasonably delaying an agency action relating to a regulatory action that would affect the rights of\u2014\n**(i)**\nprivate persons other than the person bringing the action; or\n**(ii)**\na State, local, or tribal government; and\n**(C)**\nbrought under\u2014\n**(i)**\nchapter 7 of title 5, United States Code; or\n**(ii)**\nany other statute authorizing such an action;\n**(3)**\nthe term covered consent decree means\u2014\n**(A)**\na consent decree entered into in a covered civil action; and\n**(B)**\nany other consent decree that requires agency action relating to a regulatory action that affects the rights of\u2014\n**(i)**\nprivate persons other than the person bringing the action; or\n**(ii)**\na State, local, or tribal government;\n**(4)**\nthe term covered consent decree or settlement agreement means a covered consent decree and a covered settlement agreement; and\n**(5)**\nthe term covered settlement agreement means\u2014\n**(A)**\na settlement agreement entered into in a covered civil action; and\n**(B)**\nany other settlement agreement that requires agency action relating to a regulatory action that affects the rights of\u2014\n**(i)**\nprivate persons other than the person bringing the action; or\n**(ii)**\na State, local, or tribal government.\n#### 3. Consent decree and settlement reform\n##### (a) Pleadings and preliminary matters\n**(1) In general**\nIn any covered civil action, the agency against which the covered civil action is brought shall publish the notice of intent to sue and the complaint in a readily accessible manner, including by making the notice of intent to sue and the complaint available online not later than 15 days after receiving service of the notice of intent to sue or complaint, respectively.\n**(2) Entry of a covered consent decree or settlement agreement**\nA party may not make a motion for entry of a covered consent decree or to dismiss a civil action pursuant to a covered settlement agreement until after the end of proceedings in accordance with paragraph (1) and subparagraphs (A) and (B) of paragraph (2) of subsection (d) or subsection (d)(3)(A), whichever is later.\n##### (b) Intervention\n**(1) Rebuttable presumption**\nIn considering a motion to intervene in a covered civil action or a civil action in which a covered consent decree or settlement agreement has been proposed that is filed by a person who alleges that the agency action in dispute would affect the person, the court shall presume, subject to rebuttal, that the interests of the person would not be represented adequately by the existing parties to the action.\n**(2) State, local, and tribal governments**\nIn considering a motion to intervene in a covered civil action or a civil action in which a covered consent decree or settlement agreement has been proposed that is filed by a State, local, or tribal government, the court shall take due account of whether the movant\u2014\n**(A)**\nadministers jointly with an agency that is a defendant in the action the statutory provisions that give rise to the regulatory action to which the action relates; or\n**(B)**\nadministers an authority under State, local, or tribal law that would be preempted by the regulatory action to which the action relates.\n##### (c) Settlement negotiations\nEfforts to settle a covered civil action or otherwise reach an agreement on a covered consent decree or settlement agreement shall\u2014\n**(1)**\nbe conducted pursuant to the mediation or alternative dispute resolution program of the court or by a district judge other than the presiding judge, magistrate judge, or special master, as determined appropriate by the presiding judge; and\n**(2)**\ninclude any party that intervenes in the action.\n##### (d) Publication of and comment on covered consent decrees or settlement agreements\n**(1) In general**\nNot later than 60 days before the date on which a covered consent decree or settlement agreement is filed with a court, the agency seeking to enter the covered consent decree or settlement agreement shall publish in the Federal Register and online\u2014\n**(A)**\nthe proposed covered consent decree or settlement agreement; and\n**(B)**\na statement providing\u2014\n**(i)**\nthe statutory basis for the covered consent decree or settlement agreement; and\n**(ii)**\na description of the terms of the covered consent decree or settlement agreement, including whether it provides for the award of attorneys\u2019 fees or costs and, if so, the basis for including the award.\n**(2) Public comment**\n**(A) In general**\nAn agency seeking to enter a covered consent decree or settlement agreement shall accept public comment during the period described in paragraph (1) on any issue relating to the matters alleged in the complaint in the applicable civil action or addressed or affected by the proposed covered consent decree or settlement agreement.\n**(B) Response to comments**\nAn agency shall respond to any comment received under subparagraph (A).\n**(C) Submissions to court**\nWhen moving that the court enter a proposed covered consent decree or settlement agreement or for dismissal pursuant to a proposed covered consent decree or settlement agreement, an agency shall\u2014\n**(i)**\ninform the court of the statutory basis for the proposed covered consent decree or settlement agreement and its terms;\n**(ii)**\nsubmit to the court a summary of the comments received under subparagraph (A) and the response of the agency to the comments;\n**(iii)**\nsubmit to the court a certified index of the administrative record of the notice and comment proceeding; and\n**(iv)**\nmake the administrative record described in clause (iii) fully accessible to the court.\n**(D) Inclusion in record**\nThe court shall include in the court record for a civil action the certified index of the administrative record submitted by an agency under subparagraph (C)(iii) and any documents listed in the index which any party or amicus curiae appearing before the court in the action submits to the court.\n**(3) Public hearings permitted**\n**(A) In general**\nAfter providing notice in the Federal Register and online, an agency may hold a public hearing regarding whether to enter into a proposed covered consent decree or settlement agreement.\n**(B) Record**\nIf an agency holds a public hearing under subparagraph (A)\u2014\n**(i)**\nthe agency shall\u2014\n**(I)**\nsubmit to the court a summary of the proceedings;\n**(II)**\nsubmit to the court a certified index of the hearing record; and\n**(III)**\nprovide access to the hearing record to the court; and\n**(ii)**\nthe full hearing record shall be included in the court record.\n**(4) Mandatory deadlines**\nIf a proposed covered consent decree or settlement agreement requires an agency action by a date certain, the agency shall, when moving for entry of the covered consent decree or settlement agreement or dismissal based on the covered consent decree or settlement agreement, inform the court of\u2014\n**(A)**\nany required regulatory action the agency has not taken that the covered consent decree or settlement agreement does not address;\n**(B)**\nhow the covered consent decree or settlement agreement, if approved, would affect the discharge of the duties described in subparagraph (A); and\n**(C)**\nwhy the effects of the covered consent decree or settlement agreement on the manner in which the agency discharges its duties is in the public interest.\n##### (e) Submission by the government\n**(1) In general**\nFor any proposed covered consent decree or settlement agreement that contains a term described in paragraph (2), the Attorney General or, if the matter is being litigated independently by an agency, the head of the agency shall submit to the court a certification that the Attorney General or head of the agency approves the proposed covered consent decree or settlement agreement. The Attorney General or head of the agency shall personally sign any certification submitted under this paragraph.\n**(2) Terms**\nA term described in this paragraph is\u2014\n**(A)**\nin the case of a covered consent decree, a term that\u2014\n**(i)**\nconverts into a nondiscretionary duty a discretionary authority of an agency to propose, promulgate, revise, or amend regulations;\n**(ii)**\ncommits an agency to expend funds that have not been appropriated and that have not been budgeted for the regulatory action in question;\n**(iii)**\ncommits an agency to seek a particular appropriation or budget authorization;\n**(iv)**\ndivests an agency of discretion committed to the agency by statute or the Constitution of the United States, without regard to whether the discretion was granted to respond to changing circumstances, to make policy or managerial choices, or to protect the rights of third parties; or\n**(v)**\notherwise affords relief that the court could not enter under its own authority upon a final judgment in the civil action; or\n**(B)**\nin the case of a covered settlement agreement, a term\u2014\n**(i)**\nthat provides a remedy for a failure by the agency to comply with the terms of the covered settlement agreement other than the revival of the civil action resolved by the covered settlement agreement; and\n**(ii)**\nthat\u2014\n**(I)**\ninterferes with the authority of an agency to revise, amend, or issue rules under the procedures set forth in chapter 5 of title 5, United States Code, or any other statute or Executive order prescribing rulemaking procedures for a rulemaking that is the subject of the covered settlement agreement;\n**(II)**\ncommits the agency to expend funds that have not been appropriated and that have not been budgeted for the regulatory action in question; or\n**(III)**\nfor such a covered settlement agreement that commits the agency to exercise in a particular way discretion which was committed to the agency by statute or the Constitution of the United States to respond to changing circumstances, to make policy or managerial choices, or to protect the rights of third parties.\n##### (f) Review by court\n**(1) Amicus**\nA court considering a proposed covered consent decree or settlement agreement shall presume, subject to rebuttal, that it is proper to allow amicus participation relating to the covered consent decree or settlement agreement by any person who filed public comments or participated in a public hearing on the covered consent decree or settlement agreement under paragraph (2) or (3) of subsection (d).\n**(2) Review of deadlines**\n**(A) Proposed covered consent decrees**\nFor a proposed covered consent decree, a court shall not approve the covered consent decree unless the proposed covered consent decree allows sufficient time and incorporates adequate procedures for the agency to comply with chapter 5 of title 5, United States Code, and other applicable statutes that govern rulemaking and, unless contrary to the public interest, the provisions of any Executive order that governs rulemaking.\n**(B) Proposed covered settlement agreements**\nFor a proposed covered settlement agreement, a court shall ensure that the covered settlement agreement allows sufficient time and incorporates adequate procedures for the agency to comply with chapter 5 of title 5, United States Code, and other applicable statutes that govern rulemaking and, unless contrary to the public interest, the provisions of any Executive order that governs rulemaking.\n##### (g) Annual reports\nEach agency shall submit to Congress an annual report that, for the year covered by the report, includes\u2014\n**(1)**\nthe number, identity, and content of covered civil actions brought against and covered consent decrees or settlement agreements entered against or into by the agency; and\n**(2)**\na description of the statutory basis for\u2014\n**(A)**\neach covered consent decree or settlement agreement entered against or into by the agency; and\n**(B)**\nany award of attorneys fees or costs in a civil action resolved by a covered consent decree or settlement agreement entered against or into by the agency.\n#### 4. Motions to modify consent decrees\nIf an agency moves a court to modify a covered consent decree or settlement agreement and the basis of the motion is that the terms of the covered consent decree or settlement agreement are no longer fully in the public interest due to the obligations of the agency to fulfill other duties or due to changed facts and circumstances, the court shall review the motion and the covered consent decree or settlement agreement de novo.\n#### 5. Effective date\nThis Act shall apply to\u2014\n**(1)**\nany covered civil action filed on or after the date of enactment of this Act; and\n**(2)**\nany covered consent decree or settlement agreement proposed to a court on or after the date of enactment of this Act.",
      "versionDate": "2025-12-11",
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
        "updateDate": "2026-01-07T16:56:41Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6622ih.xml"
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
      "title": "Sunshine for Regulatory Decrees and Settlements Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sunshine for Regulatory Decrees and Settlements Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To impose certain limitations on consent decrees and settlement agreements by agencies that require the agencies to take regulatory action in accordance with the terms thereof, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T06:48:24Z"
    }
  ]
}
```
