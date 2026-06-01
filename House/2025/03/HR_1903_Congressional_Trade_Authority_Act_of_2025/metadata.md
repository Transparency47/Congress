# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1903?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1903
- Title: Congressional Trade Authority Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1903
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2026-02-28T00:25:48Z
- Update date including text: 2026-02-28T00:25:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1903",
    "number": "1903",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Congressional Trade Authority Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-28T00:25:48Z",
    "updateDateIncludingText": "2026-02-28T00:25:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:04:15Z",
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
          "date": "2025-03-06T14:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "WA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NM"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "AZ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NV"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MN"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "IL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1903ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1903\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Beyer (for himself, Ms. DelBene , Mr. Schneider , Mr. Panetta , Mr. Davis of Illinois , and Ms. Chu ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Trade Expansion Act of 1962 to impose limitations on the authority of the President to adjust imports that are determined to threaten to impair national security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Congressional Trade Authority Act of 2025 .\n#### 2. Limitations on authority of president to adjust imports determined to threaten to impair national security\n##### (a) Limitation on articles for which action may be taken\nSection 232 of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862 ) is amended\u2014\n**(1)**\nby striking an article each place it appears and inserting a covered article ;\n**(2)**\nby striking any article each place it appears and inserting any covered article ;\n**(3)**\nby striking the article each place it appears and inserting the covered article ;\n**(4)**\nin the first subsection (d), by striking In the administration and all that follow through national security. ; and\n**(5)**\nby adding at the end the following:\n(i) Definitions In this section: (1) Covered article The term covered article means an article related to the development, maintenance, or protection of military equipment, energy resources, or critical infrastructure essential to national security. (2) National security The term national security \u2014 (A) means the protection of the United States from foreign aggression; and (B) does not otherwise include the protection of the general welfare of the United States. .\n##### (b) Responsibility of secretary of defense for investigations\nSection 232(b) of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), by striking the Secretary of Commerce (hereafter in the section referred to as the Secretary ) and inserting the Secretary of Defense ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking The Secretary and inserting The Secretary of Defense ; and\n**(ii)**\nby striking the Secretary of Defense and inserting the Secretary of Commerce ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the matter preceding clause (i), by striking the Secretary and inserting the Secretary of Defense ; and\n**(ii)**\nin clause (i), by striking the Secretary of Defense and inserting the Secretary of Commerce ; and\n**(B)**\nby amending subparagraph (B) to read as follows:\n(B) Upon the request of the Secretary of Defense, the Secretary of Commerce shall provide to the Secretary of Defense an assessment of the quantity of imports of any covered article that is the subject of an investigation conducted under this subsection and the circumstances under which the covered article is imported. ;\n**(3)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the first sentence, by striking the Secretary shall submit and all that follows through recommendations of the Secretary and inserting the Secretary of Defense and the Secretary of Commerce shall jointly submit to the President a report on the findings of the investigation and, based on such findings, the recommendations of the Secretary of Commerce ; and\n**(ii)**\nin the second sentence, by striking Secretary finds and all that follows through Secretary shall and inserting Secretaries find that the covered article is being imported into the United States in such quantities or under such circumstances as to be a substantial cause of a threat to impair the national security, the Secretaries shall ; and\n**(B)**\nin subparagraph (B), by striking by the Secretary ; and\n**(4)**\nin paragraph (4), by striking Secretary and inserting Secretary of Defense .\n##### (c) Determinations of president\nSection 232(c) of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking subparagraph (B);\n**(B)**\nin the matter preceding clause (i)\u2014\n**(i)**\nby striking (A) Within and inserting Within ; and\n**(ii)**\nby striking in which the Secretary and inserting that ;\n**(C)**\nby redesignating clauses (i) and (ii) as subparagraphs (A) and (B), respectively;\n**(D)**\nin subparagraph (A), as redesignated by subparagraph (C), by striking of the Secretary ; and\n**(E)**\nby amending subparagraph (B), as redesignated by subparagraph (C), to read as follows:\n(B) if the President concurs, submit to Congress, not later than 15 days after making that determination, a proposal regarding the nature and duration of the action that, in the judgment of the President, should be taken to adjust the imports of the covered article and its derivatives so that such imports will not be a substantial cause of a threat to impair the national security. ; and\n**(2)**\nby striking paragraphs (2) and (3) and inserting the following:\n(2) The President shall submit to Congress for review under subsection (f) a report describing the action proposed to be taken under paragraph (1) and specifying the reasons for such proposal. Such report shall be included in the report published under subsection (e). .\n##### (d) Congressional approval of presidential adjustment of imports\nSection 232(f) of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862(f) ) is amended to read as follows:\n(f) Congressional approval of presidential adjustment of imports; joint resolution of approval (1) In general An action to adjust imports proposed by the President in a report submitted to Congress under subsection (c)(2) shall have force and effect only if, during the period of 60 calendar days beginning on the date on which the report is submitted, a joint resolution of approval is enacted pursuant to paragraph (2). (2) Joint resolutions of approval (A) Joint resolution of approval defined In this subsection, the term joint resolution of approval means only a joint resolution of either House of Congress\u2014 (i) the title of which is as follows: A joint resolution approving the proposal of the President to take an action relating to the adjustment of imports entering into the United States in such quantities or under such circumstances as to threaten or impair the national security. ; and (ii) the sole matter after the resolving clause of which is the following: Congress approves of the proposal of the President relating to the adjustment of imports to protect the national security as described in the report submitted to Congress under section 232(c)(2) of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862(c)(2) ) on _____ relating to _____. , with the first blank space being filled with the appropriate date and the second blank space being filled with a short description of the proposed action. (B) Introduction During the period of 60 calendar days provided for under paragraph (1), a joint resolution of approval may be introduced in either House by any Member. (C) Consideration in house of representatives (i) Committee referral A joint resolution of approval introduced in the House of Representatives shall be referred to the Committee on Ways and Means. (ii) Reporting and discharge If the Committee on Ways and Means has not reported the joint resolution of approval within 10 calendar days after the date of referral, the Committee shall be discharged from further consideration of the joint resolution. (iii) Proceeding to consideration Beginning on the third legislative day after the Committee on Ways and Means reports the joint resolution of approval to the House or has been discharged from further consideration thereof, it shall be in order to move to proceed to consider the joint resolution in the House. All points of order against the motion are waived. Such a motion shall not be in order after the House has disposed of a motion to proceed on the joint resolution. The previous question shall be considered as ordered on the motion to its adoption without intervening motion. The motion shall not be debatable. A motion to reconsider the vote by which the motion is disposed of shall not be in order. (iv) Floor consideration The joint resolution of approval shall be considered as read. All points of order against the joint resolution and against its consideration are waived. The previous question shall be considered as ordered on the joint resolution to final passage without intervening motion except 2 hours of debate equally divided and controlled by the sponsor of the joint resolution (or a designee) and an opponent. A motion to reconsider the vote on passage of the joint resolution shall not be in order. (D) Consideration in the senate (i) Committee referral A joint resolution of approval introduced in the Senate shall be referred to the Committee on Finance. (ii) Reporting and discharge If the Committee on Finance has not reported the joint resolution of approval within 10 calendar days after the date of referral of the joint resolution, the Committee shall be discharged from further consideration of the joint resolution and the joint resolution shall be placed on the appropriate calendar. (iii) Proceeding to consideration Notwithstanding Rule XXII of the Standing Rules of the Senate, it is in order at any time after the Committee on Finance reports a joint resolution of approval or has been discharged from consideration of such a joint resolution to move to proceed to the consideration of the joint resolution. The motion to proceed is not debatable. The motion is not subject to a motion to postpone. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order. (iv) Rulings of the chair on procedure Appeals from the decisions of the Chair relating to the application of the rules of the Senate to the procedure relating to a joint resolution of approval shall be decided by the Senate without debate. (E) Treatment of house joint resolution in senate (i) Committee referral Except as provided in clause (ii), a joint resolution of approval that has passed the House of Representatives shall, when received in the Senate, be referred to the Committee on Finance for consideration in accordance with subparagraph (D). (ii) Consideration of house resolution If a joint resolution of approval was introduced in the Senate before receipt of a joint resolution of approval that has passed the House of Representatives\u2014 (I) the joint resolution from the House of Representatives shall, when received in the Senate, be placed on the calendar; and (II) the procedures in the Senate with respect to a joint resolution of approval introduced in the Senate shall be the same as if no joint resolution of approval had been received from the House of Representatives, except that the vote on passage in the Senate shall be on the joint resolution that passed the House of Representatives. (iii) House resolution received after passage by senate If the Senate passes a joint resolution of approval before receiving a joint resolution of approval from the House of Representatives, the joint resolution of the Senate shall be held at the desk pending receipt of the joint resolution from the House of Representatives. Upon receipt of the joint resolution of approval from the House of Representatives, such joint resolution shall be deemed to be read twice, considered, read the third time, and passed. (iv) Consideration of house resolution if no resolution introduced in senate If the Senate receives a joint resolution of approval from the House of Representatives, and no joint resolution of approval has been introduced in the Senate, the procedures described in subparagraph (D) shall apply to consideration of the joint resolution of the House. (F) Rules of house of representatives and senate This paragraph is enacted by Congress\u2014 (i) as an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, and supersedes other rules only to the extent that it is inconsistent with such rules; and (ii) with full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House. .\n##### (e) Exclusion process; report\nSection 232 of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862 ) is amended by inserting after subsection (f) the following:\n(g) Administration of exclusion process (1) In general The United States International Trade Commission shall administer a process for granting requests for the exclusion of covered articles from any actions, including actions to impose duties or quotas, taken by the President under subsection (c). (2) Requirements In administering the process required by paragraph (1), the International Trade Commission shall\u2014 (A) consider, when determining whether to grant an exclusion with respect to a covered article, if\u2014 (i) the covered article is produced in the United States and is of sufficient quality, available in sufficient quantities, and available on a reasonable timeframe; (ii) the failure to grant the exclusion would result in severe economic harm; and (iii) the failure to grant the exclusion would impair the ability of the United States to maintain effective pressure to remove an unreasonable or discriminatory practice burdening United States commerce, and further if the International Trade Commission determines that\u2014 (I) the article or a reasonable substitute is not commercially available to person requesting an exclusion under paragraph (1) with respect to a covered article; (II) the imposition of the duty with respect to the article would unreasonably increase consumer prices for day-to-day items consumed by low- or middle-income families in the United States; (III) the imposition of the duty would have an unreasonable impact on manufacturing output of the United States; (IV) the imposition of the duty would have an unreasonable impact on the ability of an entity to fulfill contracts or to build critical infrastructure; or (V) the failure to grant the exclusion is likely to result in a particular entity or entities having the ability to abuse a dominant market position; and (B) ensure that an exclusion granted with respect to a covered article is available to any person that imports the covered article; (C) not disclose business proprietary information; and (D) establish guidelines to provide for\u2014 (i) the maximum period of time that an exclusion will be in effect; (ii) applications for renewal of an exclusion; and (iii) written reasoning to a person that has requested an exclusion that the International Trade Commision has denied. (3) Publication of procedures The International Trade Commission shall publish in the Federal Register and make available on a publicly available internet website of the Commission a description of the procedures to be followed by a person requesting an exclusion under paragraph (1) with respect to a covered article. (h) Report by international trade commission Not later than 18 months after the President takes action under subsection (c) to adjust imports of a covered article, the International Trade Commission shall submit to Congress a report assessing the effects of the action on\u2014 (1) the industry to which the covered article relates; and (2) the overall economy of the United States. (i) Audit The Comptroller General of the United States shall conduct an audit on an annual basis of the exclusion process established under subsection (g)(1). .\n##### (f) Sunset\nSection 232 of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862 ), as amended by this section, is further amended by adding at the end the following:\n(i) Sunset Notwithstanding any other provision of this section, an action to adjust imports by the President in a report submitted to Congress under subsection (c)(2) with respect to a covered article shall terminate not later than the date that is three years after the date of the enactment of a joint resolution required by subsection (f) with respect to such action. .\n##### (g) Conforming amendments\nSection 232 of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862 ), as amended by this section, is further amended\u2014\n**(1)**\nin the first subsection (d), by striking the Secretary and the President each place it appears and inserting the Secretary of Defense, the Secretary of Commerce, and the President ;\n**(2)**\nby redesignating the second subsection (d) as subsection (e); and\n**(3)**\nin paragraph (1) of subsection (e), as redesignated by paragraph (2), by striking the Secretary and inserting the Secretary of Defense .\n##### (h) Effective date\nExcept as provided by subsection (h), the amendments made by this section shall apply with respect to any proposed action under section 232(c) of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862(c) ) on or after the date that is 6 years before the date of the enactment of this Act.\n##### (i) Transition rules\n**(1) Approval process for actions take before date of enactment**\n**(A) In general**\nIf, during the period specified in paragraph (2), the President makes a determination described in subsection (c) of section 232 of the Trade Expansion Act of 1962, as in effect on the day before the date of the enactment of this Act, to take action with respect to an article\u2014\n**(i)**\nnot later than 15 days after such date of enactment, the President shall resubmit to Congress the report required under that section with respect to the action; and\n**(ii)**\nthe action shall have force and effect after the day that is 75 days after such date of enactment only if, during the period of 60 calendar days beginning on the date on which the report is resubmitted under clause (i), a joint resolution of approval is enacted pursuant to subsection (f)(2) of the Trade Expansion Act of 1962, as amended by this section, with respect to the action.\n**(B) Nonapplicability of definitions**\nSubparagraph (A) shall apply with respect to an action without regard to whether the article to which the action relates is a covered article (as defined in subsection (i) of section 232 of the Trade Expansion Act of 1962, as added by this section).\n**(2) Period specified**\nThe period specified in this paragraph is the period beginning on the date that is 9 years before the date of the enactment of this Act and ending on the day before such date of enactment.\n**(3) Administration of exclusion process**\nIn the case of an action with respect to which a resolution of approval is enacted as required by paragraph (1)(A)(ii), the Secretary of Commerce shall continue to administer the process established before the date of the enactment of this Act for granting requests for the exclusion of articles from the action.\n**(4) International trade commission report**\nNot later than 180 days after the date of the enactment of this Act, the United States International Trade Commission shall submit to Congress a report described in subsection (h) of section 232 of the Trade Expansion Act of 1962, as added by this section, relating to each action taken under subsection (c) of section 232 of the Trade Expansion Act of 1962, as in effect on the day before such date of enactment, during the period specified in paragraph (2).\n**(5) Termination of actions not approved**\n**(A) In general**\nAn action described in subparagraph (B) shall terminate on the day that is 75 days after the date of the enactment of this Act.\n**(B) Action described**\nAn action described in this subparagraph is an action with respect to which\u2014\n**(i)**\nthe President made a determination described in subsection (c) of section 232 of the Trade Expansion Act of 1962, as in effect on the day before the date of the enactment of this Act, during the period specified in paragraph (2); and\n**(ii)**\na joint resolution of approval is not enacted as required by paragraph (1)(A)(ii).\n**(C) Modification of duty rate amounts**\n**(i) In general**\nAny rate of duty modified under section 232(c) of the Trade Expansion Act of 1962, as in effect on the day before the date of the enactment of this Act, pursuant to an action described in subparagraph (B) shall, on the day that is 75 days after the date of the enactment of this Act, revert to the rate of duty in effect before such modification.\n**(ii) Retroactive application for certain liquidations and reliquidations**\n**(I) In general**\nSubject to subclause (II), an entry of an article shall be liquidated or reliquidated as though such entry occurred on the date that is 75 days after the date of the enactment of this Act if\u2014\n**(aa)**\nthe rate of duty applicable to the article was modified pursuant to an action described in subparagraph (B); and\n**(bb)**\na lower rate of duty would be applicable due to the application of clause (i).\n**(II) Requests**\nA liquidation or reliquidation may be made under subclause (I) with respect to an entry only if a request therefor is filed with U.S. Customs and Border Protection not later than 255 days after the date of the enactment of this Act that contains sufficient information to enable U.S. Customs and Border Protection\u2014\n**(aa)**\nto locate the entry; or\n**(bb)**\nto reconstruct the entry if it cannot be located.\n**(III) Payment of amounts owed**\nAny amounts owed by the United States pursuant to the liquidation or reliquidation of an entry of an article under subclause (I) shall be paid, without interest, not later than 90 days after the date of the liquidation or reliquidation (as the case may be).\n**(iii) Entry defined**\nIn this paragraph, the terms entry includes a withdrawal from warehouse for consumption.",
      "versionDate": "2025-03-06",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-12T16:44:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119hr1903",
          "measure-number": "1903",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2026-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1903v00",
            "update-date": "2026-02-28"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Congressional Trade Authority Act of 2025</strong></p><p>This bill requires congressional approval for a presidential import adjustment due to a national security threat from an import and limits the adjustments to certain goods that are essential to national security.</p><p>Specifically, the bill limits the President's authority for such import adjustments to goods\u00a0related to the development, maintenance, or protection of\u00a0military equipment, energy resources, or critical infrastructure essential to national security. The bill specifies that the term <em>national security</em> (1)\u00a0means the protection of the United States from foreign aggression, and (2)\u00a0does not otherwise include the protection of the general welfare of the United States.</p><p>The bill requires the President to submit a proposal to Congress to adjust imports. Congress must then approve the proposal with a joint resolution before an import adjustment takes effect. Under current law, the President determines whether any adjustment of an import is necessary and must submit to Congress the reasons for any action taken or not taken. Currently, there is a congressional disapproval mechanism to override presidential actions related to petroleum imports.</p><p>The bill also</p><ul><li>requires the Department of Defense (currently, the Department of Commerce) to investigate the effect of these imports on national security and submit a report before the President determines whether an adjustment to an import is necessary,</li><li>establishes requirements for a process to grant requests to exclude certain goods from import adjustments, and\u00a0</li><li>applies retroactively to any proposed action\u00a0taken up to six years before the enactment of this bill.\u00a0</li></ul>"
        },
        "title": "Congressional Trade Authority Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1903.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Trade Authority Act of 2025</strong></p><p>This bill requires congressional approval for a presidential import adjustment due to a national security threat from an import and limits the adjustments to certain goods that are essential to national security.</p><p>Specifically, the bill limits the President's authority for such import adjustments to goods\u00a0related to the development, maintenance, or protection of\u00a0military equipment, energy resources, or critical infrastructure essential to national security. The bill specifies that the term <em>national security</em> (1)\u00a0means the protection of the United States from foreign aggression, and (2)\u00a0does not otherwise include the protection of the general welfare of the United States.</p><p>The bill requires the President to submit a proposal to Congress to adjust imports. Congress must then approve the proposal with a joint resolution before an import adjustment takes effect. Under current law, the President determines whether any adjustment of an import is necessary and must submit to Congress the reasons for any action taken or not taken. Currently, there is a congressional disapproval mechanism to override presidential actions related to petroleum imports.</p><p>The bill also</p><ul><li>requires the Department of Defense (currently, the Department of Commerce) to investigate the effect of these imports on national security and submit a report before the President determines whether an adjustment to an import is necessary,</li><li>establishes requirements for a process to grant requests to exclude certain goods from import adjustments, and\u00a0</li><li>applies retroactively to any proposed action\u00a0taken up to six years before the enactment of this bill.\u00a0</li></ul>",
      "updateDate": "2026-02-28",
      "versionCode": "id119hr1903"
    },
    "title": "Congressional Trade Authority Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Trade Authority Act of 2025</strong></p><p>This bill requires congressional approval for a presidential import adjustment due to a national security threat from an import and limits the adjustments to certain goods that are essential to national security.</p><p>Specifically, the bill limits the President's authority for such import adjustments to goods\u00a0related to the development, maintenance, or protection of\u00a0military equipment, energy resources, or critical infrastructure essential to national security. The bill specifies that the term <em>national security</em> (1)\u00a0means the protection of the United States from foreign aggression, and (2)\u00a0does not otherwise include the protection of the general welfare of the United States.</p><p>The bill requires the President to submit a proposal to Congress to adjust imports. Congress must then approve the proposal with a joint resolution before an import adjustment takes effect. Under current law, the President determines whether any adjustment of an import is necessary and must submit to Congress the reasons for any action taken or not taken. Currently, there is a congressional disapproval mechanism to override presidential actions related to petroleum imports.</p><p>The bill also</p><ul><li>requires the Department of Defense (currently, the Department of Commerce) to investigate the effect of these imports on national security and submit a report before the President determines whether an adjustment to an import is necessary,</li><li>establishes requirements for a process to grant requests to exclude certain goods from import adjustments, and\u00a0</li><li>applies retroactively to any proposed action\u00a0taken up to six years before the enactment of this bill.\u00a0</li></ul>",
      "updateDate": "2026-02-28",
      "versionCode": "id119hr1903"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1903ih.xml"
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
      "title": "Congressional Trade Authority Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Trade Authority Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Trade Expansion Act of 1962 to impose limitations on the authority of the President to adjust imports that are determined to threaten to impair national security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T05:33:23Z"
    }
  ]
}
```
