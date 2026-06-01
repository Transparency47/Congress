# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3835?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3835
- Title: Veterans Appeals Efficiency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3835
- Origin chamber: House
- Introduced date: 2025-06-09
- Update date: 2026-05-28T20:41:22Z
- Update date including text: 2026-05-28T20:41:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-06-24 - Committee: Subcommittee Hearings Held
- Latest action: 2025-06-09: Introduced in House

## Actions

- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-06-24 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3835",
    "number": "3835",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Veterans Appeals Efficiency Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-28T20:41:22Z",
    "updateDateIncludingText": "2026-05-28T20:41:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T16:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-24T18:12:36Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-23T18:12:29Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "CA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "CA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "FL"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "MI"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "NE"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "NY"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "NJ"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CO"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "KY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CO"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3835ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3835\nIN THE HOUSE OF REPRESENTATIVES\nJune 9, 2025 Mr. Bost (for himself, Mr. Takano , Mr. Valadao , Mr. Bilirakis , Mr. James , Mr. Bacon , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the efficiency of adjudications and appeals of claims for benefits under laws administered by Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Appeals Efficiency Act of 2025 .\n#### 2. Improvements to efficiency of adjudications and appeals of claims for benefits under laws administered by Secretary of Veterans Affairs\n##### (a) Annual report on length of adjudications\n**(1) In general**\nSection 5109B of title 38, United States Code, is amended\u2014\n**(A)**\nby striking The Secretary and inserting (a) In general.\u2014 The Secretary ; and\n**(B)**\nby adding at the end the following new subsection:\n(b) Annual report The Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate an annual report that includes, with respect to the period covered by the report\u2014 (1) the average length of time a claim (or an issue within a claim) that was remanded by the Board of Veterans\u2019 Appeals was or has been pending before the Secretary after such remand; (2) the number of cases that advanced on the docket by reason of a motion that was filed under 7107(b) of this title and on which the Board ruled, disaggregated by\u2014 (A) whether a motion was granted or denied; and (B) the reason provided for the motion; and (3) the number of appeals dismissed by the Board, disaggregated by\u2014 (A) whether or not the dismissal was by reason of the death of the appellant; and (B) in the case of a dismissal by reason of the death of the appellant, whether or not such death was a result of suicide. .\n**(2) Deadline**\nThe Secretary of Veterans Affairs shall submit the first report required by subsection (b) of section 5109B of such title (as added by paragraph (1)) by not later than one year after the date of the enactment of this Act.\n##### (b) Guidelines for advancement of cases on docket of Board\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs, in consultation with the Board of Veterans\u2019 Appeals and the General Counsel of the Department of Veterans Affairs, shall prescribe guidelines for the advancement of a case on the docket of the Board on a motion for earlier consideration and determination under section 7107(b)(3) of title 38, United States Code. Such guidelines shall include the type of evidence that may be submitted with the motion for the advancement of the case to show grounds for such a motion.\n##### (c) Requirement To track certain claims for benefits\n**(1) In general**\nChapter 51 of title 38, United States Code, is amended by inserting after section 5109B the following new section:\n5109C. Requirement to track and maintain information on certain claims for benefits; notice of certain assignments (a) In general The Secretary shall use technology to track and maintain information (including information with respect to timeliness) on\u2014 (1) claims for benefits under the laws administered by the Secretary (including issues within such claims) that are\u2014 (A) continuously pursued in accordance with\u2014 (i) sections 5104C(a) and 5110(a)(2) of this title; or (ii) any other policy established by the Secretary; (B) filed in the National Work Queue (or any successor system) but have not been assigned to an office of the Veterans Benefits Administration for adjudication; (C) afforded expeditious treatment by the Veterans Benefits Administration pursuant to section 5109B of this title or any other policy established by the Secretary; (D) remanded by the Board of Veterans\u2019 Appeals to the Secretary pursuant to section 7104 of this title; or (E) pending a hearing by the Board of Veterans\u2019 Appeals under section 7107 of this title; (2) instances in which an adjudicator of the Veterans Benefits Administration does not comply with a relevant decision of the Board of Veterans\u2019 Appeals to remand a claim for benefits under the laws administered by the Secretary (or an issue within such a claim), including any such instance in which the relevant decision concerned a failure on the part of the agency of original jurisdiction to satisfy the duty of the Secretary to assist under section 5103A of this title; (3) supplemental claims under section 5108 of this title that are filed\u2014 (A) in accordance with section 5104C(a) and section 5110(a)(2) of this title; and (B) after the date of the applicable final decision of the Secretary with respect to a claim for benefits under the laws administered by the Secretary (or an issue within such a claim); (4) first notices submitted to the Secretary of the death of individuals in receipt of benefits under the laws administered by the Secretary, disaggregated by such individuals who were\u2014 (A) assigned a fiduciary; and (B) not assigned a fiduciary. (b) Annual report (1) The Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate an annual report that includes all information maintained and tracked pursuant to subsection (a). (2) The first report required by paragraph (1) shall be submitted by not later than one year after the date of the enactment of the Veterans Appeals Efficiency Act of 2025 . .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 5109B the following new item:\nSec. 5109C. Requirement to track and maintain information on certain claims for benefits; notice of certain assignments. .\n##### (d) Improvements to Board of Veterans\u2019 Appeals\n**(1) Authority to aggregate certain claims**\n**(A) In general**\nSection 7104(a) of such title is amended by inserting after the second sentence the following new sentence: If the Chairman of the Board determines that more than one appeal involves common questions of law or fact, the Chairman may aggregate such appeals to decide such questions of law or fact. .\n**(B) Effective date**\nThe amendment made by subparagraph (A) shall take effect on the date of the enactment of this Act and apply beginning on the date on which the Secretary of Veterans Affairs completes the development of the policies and procedures required under subsection (g)(4)(A)(ii).\n**(2) Requirement to ensure substantial compliance with certain decisions**\nSuch section is further amended\u2014\n**(A)**\nby redesignating subsection (f) as subsection (g); and\n**(B)**\nby inserting after subsection (e) the following new subsection (f):\n(f) (1) The Secretary, acting through a member of the Board, shall ensure substantial compliance with any decision of the Board to remand a claim. (2) The agency of original adjudication may waive the requirement under paragraph (1) with respect to a decision of the Board to remand a claim to the Secretary, if a member of the Board determines\u2014 (A) evidence added to the evidentiary record after the date of such decision is sufficient to resolve the issues underlying such decision; or (B) such decision was unnecessary. (3) If the Secretary waives such requirement, the applicable member of the Board shall include, pursuant to subsection (d), a determination of such waiver in the decision of the Board. .\n**(3) Definition of aggregate; report**\nSuch section is further amended by adding at the end the following new subsections:\n(h) Not later than five years after the date of the enactment of the Veterans Appeals Efficiency Act of 2025 , and every five years thereafter, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the aggregation of claims by the Board under subsection (a). Each such report shall include\u2014 (1) an identification of each instance in which the Board aggregated appeals during the period covered by the report, including, for each such instance, the number of appeals that were aggregated; (2) an assessment of whether the aggregation of appeals has contributed to improved efficiency at the Board with issuing decisions on appeals; and (3) such other matters as the Secretary determines appropriate. (i) In this section, the term aggregate \u2014 (1) means any practice or procedure to collect common issues, claims, or appeals by multiple parties for the purposes of resolving such issues, claims, or appeals; and (2) includes the use of joinder, consolidation, intervention, class actions, and any other multiparty proceedings. .\n##### (e) Expansion of jurisdiction of Court of Appeals for Veterans Claims\nSection 7252 of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (b) and (c) as subsections (d) and (e), respectively; and\n**(2)**\nby inserting after subsection (a) the following new subsections:\n(b) (1) (A) In a covered proceeding in which the appellant or petitioner files a request for class certification pursuant to the rules prescribed by the Court pursuant to section 7264 of this title, the Court shall have supplemental jurisdiction over any claim for benefits under the laws administered by the Secretary\u2014 (i) that satisfies the definition of the class contained in the request for class certification; and (ii) for which the agency of original jurisdiction has issued a nonfinal decision and the claimant has filed a notice of disagreement under section 5104C(a) or section 7105 of this title, including any case in which a claimant has filed a supplemental claim within one year of a Board decision under section 5110(a)(2)(D) and 5108 of this title following a notice of disagreement and decision of the Board. (B) For purposes of subparagraph (A), a covered proceeding means\u2014 (i) an appeal over which the Court has jurisdiction pursuant to section 7266 of this title; or (ii) a request for a writ over which the Court has jurisdiction. (2) A claimant who has not opted out of an opportunity to be a member of a class action may submit a request for administrative review of such a claim under section 5104C(a) of this title during the period beginning on the date on which the named claimant of the motion for class action review submits to the Court a motion for class action review and ending on the date that is 60 days after the later of the following dates: (A) The date on which the Court issues a final decision with respect to such claim. (B) The date on which the Court issues a final decision with respect to such motion for class action review. (3) In the case of a claimant who has not opted out of an opportunity to be a member of a class action and whose claim is decided by the Board during the period when the Court is reviewing the motion for class action review the deadline for such claimant to file an appeal to the Court with respect to the decision of the Board shall be tolled if the Court denies the motion for class action review. (c) (1) In the case of a claim for benefits under the laws administered by the Secretary, the Court may remand a matter to the Board of Veterans\u2019 Appeals for the limited purpose of ordering the Board to address a question of law or fact if the Court determines the Board failed to\u2014 (A) address, in the relevant decision of the Board, an issue that\u2014 (i) the claimant or the representative of the claimant raised; or (ii) was reasonably raised by the evidentiary record of the claim; or (B) provide adequate reasons or bases for the decision of the Board with respect to such question. (2) The Court shall issue Rules that provide for each of the following: (A) When and how a party to an appeal (either the appellant or the Secretary) may request that the Court issue a limited remand. (B) The period of time within which the Board is required issue a decision on the relevant question identified in a limited remand. (C) Guidelines for when the Court may grant a request for a limited remand. (D) Guidelines for when the Court may decide sua sponte to issue a limited remand without a request from any party. (E) A requirement that the parties to an appeal for which a limited remand is issued provide notice to the Court when the Board issues its decision on the relevant question identified in the limited remand. (3) With respect to any matter remanded to the Board pursuant to paragraph (1), the Court shall\u2014 (A) retain jurisdiction over such matter; and (B) stay the proceedings of the Court on such matter until the date on which the Board issues the decision required by such remand. .\n##### (f) Study and report on common questions of law or fact before Board of Veterans\u2019 Appeals\n**(1) Study**\nThe Chairman of the Board of Veterans\u2019 Appeals shall carry out a study to identify questions of law or fact the Board commonly considers when reviewing appeals pursuant to section 7104 of title 38, United States Code, for which precedential guidance would assist the Board in issuing final decisions on such appeals. The Chairman may use artificial intelligence and other technology in carrying out such study.\n**(2) Report**\nNot later than one year after the date of the enactment of this Act, the Chairman of the Board of Veterans Appeals shall submit to the Committees on Veterans Affairs of the House of Representatives and the Senate a report that includes the findings of the study required by paragraph (1).\n##### (g) Independent assessment of potential modifications to authority of Board of Veterans\u2019 Appeals\n**(1) Agreement**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall seek to enter into an agreement with an FFRDC under which the FFRDC shall conduct an assessment of the feasibility of modifying the authority of the Board of Veterans\u2019 Appeals established under chapter 71 of title 38, United States Code, to permit the Board to issue precedential decisions with respect to questions of law or fact arising in matters before the Board.\n**(2) Report; briefings**\nIf the Secretary fails to finalize an agreement with an FFRDC under paragraph (1) before the date that is 180 days after the date on which the Secretary enters negotiations with respect to such agreement, the Secretary shall\u2014\n**(A)**\nsubmit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report that includes\u2014\n**(i)**\nan explanation of the reasons the Secretary failed to satisfy such requirement; and\n**(ii)**\nan estimate of the date on which the Secretary will finalize the agreement under paragraph (1); and\n**(B)**\nnot less frequently than once every 60 days after the date on which the Secretary failed to satisfy such requirement, provide to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a briefing on the progress of the Secretary toward finalizing such agreement.\n**(3) Assessment**\nAn FFRDC that enters into an agreement under subsection (a) shall, in consultation with veterans service organizations, veterans\u2019 and survivors\u2019 advocate groups, relevant legal experts, and the Chair of the Administrative Conference of the United States (or the designee or designees of such Chair) submit to the Secretary a written assessment that includes the following:\n**(A)**\nThe determination of the FFRDC of whether modifying the authority of the Board to permit the Board to issue precedential decisions with respect to questions of law or fact arising in matters before the Board is feasible.\n**(B)**\nAn assessment of the authority of the Board of Veterans\u2019 Appeals to aggregate, for review, more than one appeal under chapter 71 of such title that involves common questions of law or fact pursuant to section 7104 of such title, as amended by subsection (d)(1).\n**(C)**\nThe recommendations of the FFRDC with respect to rules or principles to which the Board should adhere when aggregating appeals for review pursuant to section 7104(a) of title 38, United States Code, as so amended.\n**(4) Report; implementation**\n**(A) In general**\nNot later than 90 days after the Secretary receives the assessment under subsection (b), the Secretary shall\u2014\n**(i)**\nsubmit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a copy of such assessment; and\n**(ii)**\nbegin developing policies and procedures to implement the recommendations in the assessment with respect to the authority of the Board of Veterans\u2019 Appeals referred to in paragraph (2)(B).\n**(B) Deadline**\nThe Secretary shall complete the development of the policies and procedures required under subparagraph (A)(ii) by not later than six months after the date on which the Secretary begins developing such policies and procedures.\n**(5) Definitions**\nIn this subsection:\n**(A)**\nThe term FFRDC means a federally funded research and development center.\n**(B)**\nThe term veterans service organization means an organization recognized by the Secretary for the representation of veterans under section 5902 of title 38, United States Code.",
      "versionDate": "2025-06-09",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-12-10",
        "text": "Committee on Veterans' Affairs. Hearings held."
      },
      "number": "1992",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans Appeals Efficiency Act of 2025",
      "type": "S"
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
            "name": "Administrative remedies",
            "updateDate": "2025-06-26T17:51:56Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-26T17:52:10Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-26T17:52:05Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-26T17:52:20Z"
          },
          {
            "name": "Jurisdiction and venue",
            "updateDate": "2025-06-26T17:52:15Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-26T17:52:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-24T20:24:26Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3835ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Appeals Efficiency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:23:17Z"
    },
    {
      "title": "Veterans Appeals Efficiency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the efficiency of adjudications and appeals of claims for benefits under laws administered by Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:18:18Z"
    }
  ]
}
```
