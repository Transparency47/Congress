# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6533?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6533
- Title: Military in Law Enforcement Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 6533
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-01-06T19:40:55Z
- Update date including text: 2026-01-06T19:40:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6533",
    "number": "6533",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000607",
        "district": "16",
        "firstName": "Sam",
        "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
        "lastName": "Liccardo",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Military in Law Enforcement Accountability Act",
    "type": "HR",
    "updateDate": "2026-01-06T19:40:55Z",
    "updateDateIncludingText": "2026-01-06T19:40:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-09T17:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "LA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "DC"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NV"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "AZ"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "HI"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "GA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "WA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "KY"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "OR"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MO"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "WA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MD"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "WA"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6533ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6533\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Liccardo (for himself, Ms. Houlahan , Mr. Jackson of Illinois , Mr. Fields , Mr. Doggett , Ms. Norton , Ms. Titus , Ms. Ansari , Ms. Rivas , Ms. Tokuda , Mr. Krishnamoorthi , Mr. Goldman of New York , Ms. Kelly of Illinois , Mr. Lieu , Mr. Johnson of Georgia , Ms. Garcia of Texas , Ms. Lofgren , Ms. Randall , Mr. McGarvey , Ms. Hoyle of Oregon , Mr. Bell , Mr. Casten , Ms. Strickland , Mr. Garamendi , Mr. Tran , Ms. Kamlager-Dove , Mrs. Trahan , Mrs. Fletcher , Mrs. McClain Delaney , Mr. Huffman , Ms. Jayapal , and Ms. Morrison ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 10, United States Code, to limit the authority of the Department of Defense and other Federal law enforcement personnel to support civilian law enforcement activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military in Law Enforcement Accountability Act .\n#### 2. Limitation on provision of support by Armed Forces to civilian law enforcement activities\n##### (a) In general\nChapter 15 of title 10, United States Code, is amended by inserting after section 274 the following new section:\n274a. Limitation on provision of support (a) In general The Secretary of Defense may provide support under section 272, 273, or 274 of this title only if the President first submits to Congress a notification and written justification for the support that includes\u2014 (1) the agency to which the support is provided; (2) the budget, implementation timeline with milestones, anticipated delivery schedule, and completion date for the purpose or project for which the support is provided; (3) the source and planned expenditure of funds provided for such purpose or project; (4) a description of the arrangements, if any, for the sustainment of such purpose or project and the source of funds to support sustainment of the capabilities and performance outcomes achieved using the support, if applicable; (5) a description of the objectives for such purpose or project and an evaluation framework to be used to develop capability and performance metrics associated with operational outcomes for the recipient of the support; and (6) information, including the amount, type, and purpose, about the support provided to the agency during the three fiscal years preceding the fiscal year for which the support covered by the notification and justification is provided. (b) Limitation on timing (1) In general The Secretary of Defense may not provide support under section 272, 273, or 274 of this title for a period that exceeds 30 days unless a joint resolution of approval is enacted that approves the provision of such support for a longer period. (2) Joint resolution of approval In this subsection, the term joint resolution of approval means only a joint resolution of either House of Congress\u2014 (A) the title of which is as follows: A joint resolution approving the provision by the Department of Defense of support to civilian law enforcement for a period of more than 30 days. ; and (B) the sole matter after the resolving clause of which is the following: Congress approves of the provision of support under section 272, 273, or 274 of title 10, United States Code, with respect to ______ for a period not to exceed _____. , with the first blank space being filled with a short description of the proposed action and the second blank space being filled with the appropriate period following the date of adoption of the resolution. (3) Introduction A joint resolution of approval may be introduced\u2014 (A) in the Senate, by the majority leader (or the majority leader's designee) or the minority leader (or the minority leader's designee); and (B) in the House of Representatives, by the majority leader or the minority leader. (4) Consideration in the Senate (A) Committee referral A joint resolution of approval introduced in the Senate shall be referred to the Committee on Armed Services. (B) Reporting and discharge If the Committee on Armed Services has not reported a joint resolution of approval within 10 calendar days after the date of referral of the joint resolution, that committee shall be discharged from further consideration of the joint resolution and the joint resolution shall be placed on the appropriate calendar. (C) Proceeding to consideration Notwithstanding Rule XXII of the Standing Rules of the Senate, it is in order at any time after the Committee on Armed Services reports a joint resolution of approval to the Senate or has been discharged from consideration of such a joint resolution (even though a previous motion to the same effect has been disagreed to) to move to proceed to the consideration of the joint resolution, and all points of order against the joint resolution (and against consideration of the joint resolution) are waived. The motion to proceed is not debatable. The motion is not subject to a motion to postpone. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order. (D) Approval of resolution Approval by the Senate of a joint resolution of approval shall require the affirmative vote of three-fifths of Members of the Senate, duly chosen and sworn. (E) Rulings of the chair on procedure Appeals from the decisions of the Chair relating to the application of the rules of the Senate, as the case may be, to the procedure relating to a joint resolution of approval shall be decided without debate. (F) Consideration of veto messages Debate in the Senate of any veto message with respect to a joint resolution of approval, including all debatable motions and appeals in connection with the joint resolution, shall be limited to 10 hours, to be equally divided between, and controlled by, the majority leader and the minority leader or their designees. (5) Floor consideration in House of Representatives If a committee of the House of Representatives to which a joint resolution of approval has been referred has not reported the joint resolution within 10 calendar days after the date of referral, that committee shall be discharged from further consideration of the joint resolution. (6) Rules relating to Senate and House of Representatives (A) Treatment of House joint resolution in Senate (i) Receipt before passage of Senate resolution If, before the passage by the Senate of a joint resolution of approval, the Senate receives an identical joint resolution from the House of Representatives, the following procedures shall apply: (I) That joint resolution shall not be referred to a committee. (II) With respect to that joint resolution\u2014 (aa) the procedure in the Senate shall be the same as if no joint resolution had been received from the House of Representatives; but (bb) the vote on passage shall be on the joint resolution from the House of Representatives. (ii) Receipt following passage of Senate resolution If, following passage of a joint resolution of approval in the Senate, the Senate receives an identical joint resolution from the House of Representatives, that joint resolution shall be placed on the appropriate Senate calendar. (iii) No companion resolution If a joint resolution of approval is received from the House, and no companion joint resolution has been introduced in the Senate, the Senate procedures under this subsection shall apply to the House joint resolution. (B) Treatment of Senate joint resolution in House In the House of Representatives, the following procedures shall apply to a joint resolution of approval received from the Senate (unless the House has already passed a joint resolution relating to the same proposed action): (i) The joint resolution shall be referred to the Committee on Armed Services. (ii) If the Committee on Armed Services has not reported the joint resolution within 2 calendar days after the date of referral, that committee shall be discharged from further consideration of the joint resolution. (iii) Beginning on the third legislative day after the Committee on Armed Services reports the joint resolution to the House or has been discharged from further consideration thereof, it shall be in order to move to proceed to consider the joint resolution in the House. All points of order against the motion are waived. Such a motion shall not be in order after the House has disposed of a motion to proceed on the joint resolution. The previous question shall be considered as ordered on the motion to its adoption without intervening motion. The motion shall not be debatable. A motion to reconsider the vote by which the motion is disposed of shall not be in order. (iv) The joint resolution shall be considered as read. All points of order against the joint resolution and against its consideration are waived. The previous question shall be considered as ordered on the joint resolution to final passage without intervening motion except 2 hours of debate equally divided and controlled by the sponsor of the joint resolution (or a designee) and an opponent. A motion to reconsider the vote on passage of the joint resolution shall not be in order. (C) Application to revenue measures The provisions of this paragraph shall not apply in the House of Representatives to a joint resolution of approval that is a revenue measure. (7) Rules of Senate and House of Representatives This subsection is enacted by Congress\u2014 (A) as an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, and supersedes other rules only to the extent that it is inconsistent with such rules; and (B) with full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 15 of such title is amended by inserting after the item relating to section 274 the following new item:\n274a. Limitation on provision of support. .\n##### (c) Conforming amendments\n**(1) Use of military equipment**\nSection 272 of title 10, United States Code, is amended by inserting section 274a of this title and after in accordance with .\n**(2) Training and advising civilian law enforcement officials**\nSection 273 of title 10, United States Code, is amended by inserting section 274a of this title and after in accordance with .\n**(3) Maintenance and operation of equipment**\nSection 274 of title 10, United States Code, is amended by inserting section 274a of this title and after in accordance with each place it appears.\n#### 3. Prohibition on simultaneous service in the Department of Defense and civilian law enforcement\n##### (a) In general\nChapter 49 of title 10, United States Code, is amended by adding at the end the following new section:\n990. Prohibition on simultaneous service in the Department of Defense and civilian law enforcement (a) Prohibition Except as provided in subsection (b), an individual serving in any capacity in the Department of Defense, whether in the Armed Forces or in a civilian position, may not, while so serving, serve in any capacity in any element of civilian law enforcement outside of the Department of Defense. (b) Exceptions (1) In general The prohibition under subsection (a) shall not to apply to a member of a reserve component named in section 10101 of this title who serves in an element of civilian law enforcement outside of the Department of Defense in their civilian capacity. (2) Active duty A member described in paragraph (1) who is called or ordered to active duty shall formally and officially recuse himself or herself from civilian law enforcement duties. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 49 of such title is amended by adding at the end the following new item:\n990. Prohibition on simultaneous service in the Department of Defense and civilian law enforcement. .\n#### 4. Expansion of requirements for Armed Forces and Federal law enforcement personnel when assisting civil authorities\n##### (a) In general\nSection 723(a) of title 10, United States Code, is amended by striking to respond to a civil disturbance .\n##### (b) Conforming and clerical amendments\n**(1) Conforming amendment**\nThe heading for section 723 of title 10, United States Code, is amended by striking in response to civil disturbances .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 41 of title 10, United States Code, is amended by striking the item relating to section 723 and inserting the following new item:\n723. Support of Federal authorities: requirement for use of members of the Armed Forces and Federal law enforcement personnel. .\n#### 5. Private right of action\n##### (a) In general\nAny person, State, or local government aggrieved of a violation of this Act or an amendment made by this Act by the Federal Government, or an officer or employee thereof, may bring a civil action in an appropriate district court of the United States.\n##### (b) Relief\nIn a civil action brought under subsection (a), the court may award injunctive or other equitable relief and damages.",
      "versionDate": "2025-12-09",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T19:40:55Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6533ih.xml"
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
      "title": "Military in Law Enforcement Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Military in Law Enforcement Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to limit the authority of the Department of Defense and other Federal law enforcement personnel to support civilian law enforcement activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:22Z"
    }
  ]
}
```
