# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/513?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/513
- Title: Offshore Lands Authorities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 513
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-05-12T19:16:29Z
- Update date including text: 2026-05-12T19:16:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-05-20 - Committee: Subcommittee Hearings Held
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-05-20 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/513",
    "number": "513",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Offshore Lands Authorities Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-12T19:16:29Z",
    "updateDateIncludingText": "2026-05-12T19:16:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
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
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:11:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-05-20T21:14:15Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-05-13T14:57:58Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-16T14:11:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IN"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WV"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "OK"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MO"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MD"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AL"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MN"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "OH"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "IN"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "SD"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr513ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 513\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Higgins of Louisiana (for himself, Mr. Hunt , Mr. Weber of Texas , Mr. Burchett , Mr. Shreve , Mr. Meuser , Mr. Arrington , Mrs. Miller of West Virginia , Mr. Crenshaw , Mr. Brecheen , Ms. Van Duyne , Mr. Perry , Mr. Tiffany , Mrs. Miller of Illinois , Mr. Ogles , Mr. Burlison , Mr. Clyde , Mr. Biggs of Arizona , Mr. Harris of Maryland , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo nullify certain Presidential withdrawals of unleased offshore land, amend the Outer Continental Shelf Lands Act to establish limits on the authority of the President to withdraw unleased offshore land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Offshore Lands Authorities Act of 2025 .\n#### 2. Nullification of Presidential withdrawals of unleased offshore land\nThe following Presidential withdrawals of unleased offshore land shall have no force or effect:\n**(1)**\nThe Presidential Memorandum of December 20, 2016, titled Memorandum on Withdrawal of Certain Portions of the United States Arctic Outer Continental Shelf From Mineral Leasing (relating to the Chukchi Sea Planning Area and the Beaufort Sea Planning Area).\n**(2)**\nThe Presidential Memorandum of December 16, 2014, titled Memorandum on Withdrawal of Certain Areas of the United States Outer Continental Shelf From Leasing Disposition (relating to the North Aleutian Basin Planning Area).\n**(3)**\nSection 3 of Executive Order 13754 (81 Fed. Reg. 90669; relating to Northern Bering Sea climate resilience).\n**(4)**\nSection 4(b) of Executive Order 13990 (86 Fed. Reg. 7037; relating to reinstating Executive Order 13754 and the Presidential Memorandum of December 20, 2016).\n**(5)**\nThe Presidential Memorandum of March 13, 2023, titled Memorandum on Withdrawal of Certain Areas off the United States Arctic Coast of the Outer Continental Shelf from Oil or Gas Leasing (relating to the Beaufort Planning Area).\n**(6)**\nThe Presidential Memorandum of December 20, 2016, titled Memorandum on Withdrawal of Certain Areas off the Atlantic Coast on the Outer Continental Shelf From Mineral Leasing (relating to canyons and canyon complexes offshore the Atlantic coast).\n**(7)**\nThe Presidential Memorandum of January 6, 2025, titled Memorandum on the Withdrawal of Certain Areas of the United States Outer Continental Shelf from Oil or Natural Gas Leasing (relating to the Gulf of Mexico, Atlantic, and Pacific areas).\n**(8)**\nThe Presidential Memorandum of January 6, 2025, titled Memorandum on the Withdrawal of Certain Areas of the United States Outer Continental Shelf from Oil or Natural Gas Leasing (relating to the Northern Bering Sea Climate Resilience Area).\n#### 3. Limitation of authority of the President to withdraw unleased offshore lands\nSection 12(a) of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1341(a) ) is amended\u2014\n**(1)**\nby striking (a) The President and inserting the following:\n(a) Withdrawal of unleased lands by the President (1) In general Except as provided in paragraphs (2) and (3), the President ;\n**(2)**\nby inserting Beginning on the date of enactment of the Offshore Lands Authorities Act of 2025 , the President shall transmit a withdrawal made under the preceding sentence to the President of the Senate and the Speaker of the House of Representatives. after outer Continental Shelf. ; and\n**(3)**\nby adding at the end the following:\n(2) Limitations (A) Acres A withdrawal under paragraph (1) may not exceed an area larger than 150,000 acres in total or contiguous with any other withdrawal under such paragraph. (B) Period A withdrawal under paragraph (1) may not be made for a period longer than 20 years. (C) Cumulative withdrawals No President may, under paragraph (1), withdraw more than 500,000 acres cumulatively without obtaining Congressional approval. (3) Assessments required The President may not withdraw unleased lands of the outer Continental Shelf under paragraph (1) unless\u2014 (A) the Secretary completed a quantitative and qualitative geophysical and geological mineral resource assessment of the lands to be withdrawn during the 5-year period ending on the date of such withdrawal; (B) the Secretary, in consultation with the Secretary of Commerce, the Secretary of Energy, the Secretary of Defense, and the Secretary of Agriculture, completed an assessment of the economic, energy, and national security value of mineral deposits identified in the mineral resource assessment completed under subparagraph (A); (C) the Secretary completed an assessment of the expected reduction in future Federal revenues resulting from the proposed withdrawal to the Treasury, States (including from allocations made under section 105 of the Gulf of Mexico Energy Security Act of 2006 ( 43 U.S.C. 1331 note)), the Land and Water Conservation Fund, and the Historic Preservation Fund; and (D) the Secretary submits to the Committees on Natural Resources, Agriculture, Armed Services, Energy and Commerce, and Foreign Affairs of the House of Representatives and the Committees on Agriculture, Nutrition, and Forestry, Armed Services, Energy and Natural Resources, and Foreign Relations of the Senate a report that includes the results of the assessments completed under this subsection. (4) Congressional disapproval procedure (A) Joint resolution defined For the purposes of this paragraph, the term joint resolution means only a joint resolution, which may not have a preamble, the matter after the resolving clause of which is as follows: That Congress disapproves the withdrawal made under section 12(a)(1) of the Outer Continental Shelf Lands Act on ____, relating to ____, and such withdrawal shall have no force or effect. (the blank spaces being appropriately filled in). (B) Referral A joint resolution described in subparagraph (A) shall be referred to the committees in each House of Congress with jurisdiction. (C) Discharge In the Senate, if the committee to which is referred a joint resolution described in subparagraph (A) has not reported such joint resolution (or a joint resolution aimed at the same Presidential withdrawal) at the end of 20 calendar days after the submission or introduction of legislation to disapprove the withdrawal, such committee may be discharged from further consideration of such joint resolution and placed on the appropriate calendar of the Senate upon a petition supported in writing by 30 Members of the Senate. (D) Floor consideration (i) In general In the Senate, when the committee to which a joint resolution is referred has reported, or when a committee is discharged (under subparagraph (C)) from further consideration of, a joint resolution described in subparagraph (A), it is at any time thereafter in order (even though a previous motion to the same effect has been disagreed to) for a motion to proceed to the consideration of the joint resolution, and all points of order against the joint resolution (and against consideration of joint resolution) are waived. The motion is not subject to amendment, to a motion to postpone, or to a motion to proceed to the consideration of other business. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order. If a motion to proceed to the consideration of the joint resolution is agreed to, the joint resolution shall remain the unfinished business of the Senate until disposed of. (ii) Debate In the Senate, debate on the joint resolution, and on all debatable motions and appeals in connection therewith, shall be limited to not more than 10 hours, which shall be divided equally between those favoring and those opposing the resolution. A motion further to limit debate is in order and not debatable. An amendment to, or a motion to postpone, or a motion to proceed to the consideration of other business, or a motion to recommit the resolution is not in order. (iii) Final passage In the Senate, immediately following the conclusion of the debate on a resolution described in subparagraph (A), and a single quorum call at the conclusion of the debate if requested in accordance with the rules of the Senate, the vote on final passage of the resolution shall occur. (iv) Appeals In the Senate, appeals from the decisions of the Chair relating to the application of the rules of the Senate to the procedure relating to a resolution described in subparagraph (A) shall be decided without debate. (v) Treatment if other House has acted If, before the passage by one House of a resolution of that House described in subparagraph (A), that House receives from the other House a resolution described in subparagraph (A), then the following procedures shall apply: (I) Nonreferral The resolution of the other House shall not be referred to a committee. (II) Final passage With respect to a resolution described in subparagraph (A) of the House receiving the resolution\u2014 (aa) the procedure in that House shall be the same as if no resolution had been received from the other House; but (bb) the vote on final passage shall be on the resolution of the other House. (vi) Debate on veto message In the Senate, debate on a veto message from the President on a joint resolution described in subparagraph (A), including all debatable motions and appeals in connection therewith, shall be limited to not more than 10 hours, equally divided between those favoring and those opposing the resolution. A motion further to limit debate is in order and not debatable. No amendment to the veto message shall be in order. The vote on passage of the joint resolution following the veto message shall occur immediately following the conclusion of debate. (E) Constitutional authority Subparagraphs (A) through (D) are enacted by Congress\u2014 (i) as an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such it is deemed a part of the rules of each House, respectively, but applicable only with respect to procedure to be followed in this paragraph, and it supersedes other rules only to the extent that it is inconsistent with such rules; and (ii) with full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House. (F) Lack of effect or continuance; Substantially similar withdrawals (i) Lack of effect or continuance A withdrawal made under section 12(a)(1) of the Outer Continental Shelf Lands Act shall not take effect (or continue), if the Congress enacts a joint resolution of disapproval, described under subparagraph (A), of the withdrawal. (ii) Substantially similar withdrawals A withdrawal that does not take effect (or does not continue) under clause (i) may not be reissued in substantially the same form, and a new withdrawal that is substantially the same as such a withdrawal may not be issued, unless the reissued or new withdrawal is specifically authorized by a law enacted after the date of the joint resolution disapproving the original withdrawal. (G) Judicial review No determination, finding, action, or omission under this paragraph shall be subject to judicial review. (H) Submission of covered agency action to Congress (i) Requirement to submit Any covered agency action subject to the disapproval procedures under this subsection shall be submitted to Congress by the agency responsible for the action. Such submission must include the text of the agency action, a concise summary of the action, and the date on which the action was taken. (ii) Transmittal For purposes of this subsection, the date of submission of the covered agency action to Congress shall be the later of\u2014 (I) the date on which the agency submits the action to both the President of the Senate and the Speaker of the House of Representatives; or (II) the date on which the agency makes the action publicly available in the Federal Register or by another publicly accessible method. (iii) Start of procedures The submission of the covered agency action under clause (i) shall trigger the expedited parliamentary procedures set forth in this subsection. No resolution under this subsection may be considered in either chamber until such submission has occurred. (iv) Notice of submission Upon receipt of a covered agency action, the President of the Senate and the Speaker of the House of Representatives shall cause a notice of such submission to be published in the Congressional Record on the next calendar day of their respective chambers. (5) Integration with 5-year oil and gas leasing program The President may not make a withdrawal under paragraph (1) that conflicts with areas included in a lease sale scheduled under an oil and gas leasing program approved under Section 18. .",
      "versionDate": "2025-01-16",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-05-22T14:54:36Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-05-22T14:48:56Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-05-22T14:54:42Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2025-05-22T14:56:44Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-05-22T14:55:51Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-05-22T14:55:46Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-05-22T14:47:48Z"
          },
          {
            "name": "Seashores and lakeshores",
            "updateDate": "2025-05-22T14:56:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-02-13T19:51:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "House",
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
          "measure-id": "id119hr513",
          "measure-number": "513",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2026-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr513v00",
            "update-date": "2026-05-12"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Offshore Lands Authorities Act of 2025</strong></p><p>This bill limits the withdrawal of unleased lands of the Outer Continental Shelf (OCS) from areas that may be leased for mineral\u00a0development and nullifies certain past withdrawals. The\u00a0OCS includes\u00a0the federally managed ocean area extending from the outer\u00a0boundaries of state-controlled waters (generally 3 nautical miles [nmi] from shore) to 200 nmi from shore, with some exceptions.</p><p>Specifically, the bill limits the President's authority to restrict offshore development of minerals, such as oil and gas, on the\u00a0OCS. For example, the bill\u00a0(1) caps the number of acres of OCS lands that a President may withdraw from areas that may be leased; (2) prohibits withdrawals from being made for a period longer than 20 years; (3) prohibits the President from making withdrawals of unleased land that conflict with areas included in lease sales scheduled under approved oil and gas leasing programs; and (4) prohibits the President from withdrawing unleased lands unless the Department of the Interior has completed assessments addressing issues such\u00a0as mineral resources and the national security, economic, and energy value of the identified mineral deposits.</p><p>The President must also obtain\u00a0congressional approval before withdrawing more than 500,000 acres cumulatively. Further, the bill gives Congress the authority to review and disapprove withdrawals\u00a0by enacting a joint resolution.</p><p>In addition, the bill nullifies\u00a0certain presidential memoranda and executive orders related to withdrawing unleased land from areas that may be leased for the development of oil, gas, or other\u00a0minerals on the\u00a0OCS.</p>"
        },
        "title": "Offshore Lands Authorities Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr513.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Offshore Lands Authorities Act of 2025</strong></p><p>This bill limits the withdrawal of unleased lands of the Outer Continental Shelf (OCS) from areas that may be leased for mineral\u00a0development and nullifies certain past withdrawals. The\u00a0OCS includes\u00a0the federally managed ocean area extending from the outer\u00a0boundaries of state-controlled waters (generally 3 nautical miles [nmi] from shore) to 200 nmi from shore, with some exceptions.</p><p>Specifically, the bill limits the President's authority to restrict offshore development of minerals, such as oil and gas, on the\u00a0OCS. For example, the bill\u00a0(1) caps the number of acres of OCS lands that a President may withdraw from areas that may be leased; (2) prohibits withdrawals from being made for a period longer than 20 years; (3) prohibits the President from making withdrawals of unleased land that conflict with areas included in lease sales scheduled under approved oil and gas leasing programs; and (4) prohibits the President from withdrawing unleased lands unless the Department of the Interior has completed assessments addressing issues such\u00a0as mineral resources and the national security, economic, and energy value of the identified mineral deposits.</p><p>The President must also obtain\u00a0congressional approval before withdrawing more than 500,000 acres cumulatively. Further, the bill gives Congress the authority to review and disapprove withdrawals\u00a0by enacting a joint resolution.</p><p>In addition, the bill nullifies\u00a0certain presidential memoranda and executive orders related to withdrawing unleased land from areas that may be leased for the development of oil, gas, or other\u00a0minerals on the\u00a0OCS.</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119hr513"
    },
    "title": "Offshore Lands Authorities Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Offshore Lands Authorities Act of 2025</strong></p><p>This bill limits the withdrawal of unleased lands of the Outer Continental Shelf (OCS) from areas that may be leased for mineral\u00a0development and nullifies certain past withdrawals. The\u00a0OCS includes\u00a0the federally managed ocean area extending from the outer\u00a0boundaries of state-controlled waters (generally 3 nautical miles [nmi] from shore) to 200 nmi from shore, with some exceptions.</p><p>Specifically, the bill limits the President's authority to restrict offshore development of minerals, such as oil and gas, on the\u00a0OCS. For example, the bill\u00a0(1) caps the number of acres of OCS lands that a President may withdraw from areas that may be leased; (2) prohibits withdrawals from being made for a period longer than 20 years; (3) prohibits the President from making withdrawals of unleased land that conflict with areas included in lease sales scheduled under approved oil and gas leasing programs; and (4) prohibits the President from withdrawing unleased lands unless the Department of the Interior has completed assessments addressing issues such\u00a0as mineral resources and the national security, economic, and energy value of the identified mineral deposits.</p><p>The President must also obtain\u00a0congressional approval before withdrawing more than 500,000 acres cumulatively. Further, the bill gives Congress the authority to review and disapprove withdrawals\u00a0by enacting a joint resolution.</p><p>In addition, the bill nullifies\u00a0certain presidential memoranda and executive orders related to withdrawing unleased land from areas that may be leased for the development of oil, gas, or other\u00a0minerals on the\u00a0OCS.</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119hr513"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr513ih.xml"
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
      "title": "Offshore Lands Authorities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Offshore Lands Authorities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To nullify certain Presidential withdrawals of unleased offshore land, amend the Outer Continental Shelf Lands Act to establish limits on the authority of the President to withdraw unleased offshore land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T09:18:34Z"
    }
  ]
}
```
