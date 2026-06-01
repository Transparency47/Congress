# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3106
- Title: No Nuclear Testing Without Approval Act
- Congress: 119
- Bill type: S
- Bill number: 3106
- Origin chamber: Senate
- Introduced date: 2025-11-05
- Update date: 2025-12-05T22:02:29Z
- Update date including text: 2025-12-05T22:02:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-05: Introduced in Senate
- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-11-05: Introduced in Senate

## Actions

- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-05",
    "latestAction": {
      "actionDate": "2025-11-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3106",
    "number": "3106",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "No Nuclear Testing Without Approval Act",
    "type": "S",
    "updateDate": "2025-12-05T22:02:29Z",
    "updateDateIncludingText": "2025-12-05T22:02:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-05",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-05",
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
          "date": "2025-11-05T19:12:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NV"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NM"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NM"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "AZ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3106is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3106\nIN THE SENATE OF THE UNITED STATES\nNovember 5, 2025 Ms. Cortez Masto (for herself, Ms. Rosen , Mr. Luj\u00e1n , Mr. Heinrich , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the approval of Congress before explosive nuclear testing may be resumed.\n#### 1. Short title\nThis Act may be cited as the No Nuclear Testing Without Approval Act .\n#### 2. Requirement for approval of Congress for conduct of explosive nuclear testing\nSection 4210(a) of the Atomic Energy Defense Act ( 50 U.S.C. 2530(a) ) is amended to read as follows:\n(a) Explosive nuclear testing (1) In general No explosive nuclear testing may be conducted by the United States after the date of the enactment of the No Nuclear Testing Without Approval Act unless\u2014 (A) (i) a foreign state conducts an explosive nuclear test after that date; or (ii) there is a technical need for such testing; (B) not less than 180 days before the date proposed to conduct such testing, the President submits to Congress a notification described in paragraph (2) with respect to such testing; and (C) a joint resolution approving the testing with respect to which the notification is submitted under subparagraph (B) is enacted into law\u2014 (i) in the case of testing proposed to be conducted after a foreign state conducts an explosive nuclear test\u2014 (I) without use of expedited procedures under paragraph (3); but (II) requiring, for passage in the Senate, the affirmative vote of two-thirds of Senators, duly chosen and sworn; or (ii) in the case of testing proposed to be conducted because there is a technical need for such testing, pursuant to paragraph (3). (2) Notification described (A) In general A notification described in this paragraph with respect to a proposal to conduct explosive nuclear testing shall include\u2014 (i) a description of the testing proposed to be conducted; (ii) a statement of the reasons for conducting the testing, including\u2014 (I) whether or not there is a technical need for conducting the testing; (II) if there is a technical need for conducting the testing\u2014 (aa) a description of the technical need; (bb) an assessment of alternative options for addressing the need; (cc) an explanation of why those options were not selected; and (dd) a description of engagement with the Governor of the State in which explosive nuclear testing would occur; and (III) if the reason for conducting the testing is in response to a geopolitical event under the responsibility of the President acting as the Commander in Chief of the Armed Forces, a detailed explanation of why the testing would be in the supreme national interest of the United States; (iii) an estimate of the timelines and costs of conducting the testing; and (iv) any other information the President considers relevant. (B) Form A notification described in subparagraph (A) shall be submitted in unclassified form but may include a classified annex. (3) Joint resolution of approval for explosive nuclear testing for which there is a technical need (A) Joint resolution of approval defined In this paragraph, the term joint resolution of approval means a joint resolution of either House of Congress the sole matter after the resolving clause of which is the following: Congress approves of the proposal of the President to conduct explosive nuclear testing for which there is a technical need, notice of which was submitted to Congress under section 4210(a) of the Atomic Energy Defense Act ( 50 U.S.C. 2530(a) ) on ____. , with the blank space being filled with the appropriate date. (B) Introduction; referral A joint resolution of approval\u2014 (i) may be introduced in either House by any member; and (ii) shall be referred\u2014 (I) in the Senate, to the Committee on Armed Services of the Senate; and (II) in the House of Representatives, to the Committee on Armed Services of the House of Representatives. (C) Consideration in House of Representatives (i) Reporting and discharge The Committee on Armed Services of the House of Representatives shall report a joint resolution of approval to the House not later than 60 calendar days after the date of receipt of the notification submitted under paragraph (1)(B). If the committee fails to report the joint resolution within that period, the committee shall be discharged from further consideration of the joint resolution and the joint resolution shall be referred to the appropriate calendar. (ii) Proceeding to consideration After the Committee on Armed Services of the House of Representatives reports the joint resolution of approval to the House or has been discharged from its consideration, it shall be in order, not later than the 120th day after Congress receives the notification submitted under paragraph (1)(B), to move to proceed to consider the joint resolution in the House. All points of order against the motion are waived. Such a motion shall not be in order after the House has disposed of a motion to proceed on the joint resolution. The previous question shall be considered as ordered on the motion to its adoption without intervening motion. The motion shall not be debatable. A motion to reconsider the vote by which the motion is disposed of shall not be in order. (iii) Consideration The joint resolution of approval shall be considered as read. All points of order against the joint resolution and against its consideration are waived. The previous question shall be considered as ordered on the joint resolution to its passage without intervening motion except 24 hours of debate equally divided and controlled by the proponent and an opponent. A motion to reconsider the vote on passage of the joint resolution shall not be in order. (D) Consideration in Senate (i) Reporting and discharge The Committee on Armed Services of the Senate shall report a joint resolution of approval to the Senate not later than 60 calendar days after the date of receipt of the notification submitted under paragraph (1)(B). If the committee fails to report the joint resolution within that period, the committee shall be discharged from further consideration of the joint resolution and the joint resolution shall be placed on the Calendar of Business. (ii) Floor consideration (I) In general Notwithstanding Rule XXII of the Standing Rules of the Senate, it is in order at any time after the Committee on Armed Services reports a joint resolution of approval or is discharged from consideration of a joint resolution of approval to move to proceed to the consideration of the joint resolution, and all points of order against the motion to proceed to the joint resolution (and against consideration of the joint resolution) are waived. The motion to proceed is not debatable. The motion is not subject to a motion to postpone. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order. If a motion to proceed to the consideration of the resolution is agreed to, the joint resolution shall remain the unfinished business until disposed of. (II) Consideration Consideration of a joint resolution of approval, and on all debatable motions in connection therewith, shall be limited to not more than 10 hours, which shall be divided equally between the majority and minority leaders or their designees. A motion further to limit debate is in order and not debatable. An amendment to, a motion to postpone, or a motion to proceed to the consideration of other business, or a motion to recommit the joint resolution is not in order. (III) Vote on passage The vote on passage shall occur immediately following the conclusion of the debate on a joint resolution of approval, and a single quorum call at the conclusion of the debate if requested in accordance with the rules of the Senate. Passage of the joint resolution shall require the affirmative vote of two-thirds of Senators, duly chosen and sworn. (IV) Rulings of the chair on procedure Appeals from the decisions of the Chair relating to the application of the rules of the Senate, as the case may be, to the procedure relating to a joint resolution of approval shall be decided without debate. (E) Rules relating to senate and house of representatives (i) Coordination with action by other house If, before the passage by one House of a joint resolution of that House, that House receives from the other House a joint resolution of approval that is identical to the joint resolution of the House receiving the resolution, then the following procedures shall apply: (I) The joint resolution of the other House shall not be referred to a committee. (II) With respect to a joint resolution of the House receiving the resolution\u2014 (aa) the procedure in that House shall be the same as if no joint resolution had been received from the other House; but (bb) the vote on passage shall\u2014 (AA) require the affirmative vote of two-thirds of Senators, duly chosen and sworn, for passage; and (BB) be on the joint resolution of the other House. (ii) Treatment of joint resolution of other house If one House fails to introduce or consider a joint resolution under this section, the joint resolution of the other House shall be entitled to expedited floor procedures under this paragraph. (iii) Treatment of companion measures If, following passage of the joint resolution in the Senate, the Senate then receives an identical resolution from the House of Representatives, the resolution of the House shall not be debatable. (iv) Consideration of veto messages If the President vetoes a joint resolution of approval, debate on a veto message in the Senate shall be 1 hour equally divided between the majority and minority leaders or their designees. (F) Rules of the House of Representatives and Senate This paragraph enacted by the Senate and the House of Representatives\u2014 (i) as an exercise of the rulemaking power of the Senate and House, respectively, and as such it is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House in the case of a joint resolution of approval, and it supersedes other rules only to the extent that it is inconsistent with such rules; and (ii) with full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House. (5) Definitions In this subsection: (A) Explosive nuclear testing The term explosive nuclear testing \u2014 (i) means testing involving the explosive compression or assembly of fissile material to exceed critical mass with the attendant release of any nuclear energy from fission processes; and (ii) does not include subcritical experiments carried out as part of the stockpile stewardship program under section 4201, laser fusion experiments, or other inertial confinement fusion experiments however driven. (B) Technical need The term technical need , with respect to explosive nuclear testing, means that all officials specified in section 4205(b) determine that an explosive nuclear test is necessary to resolve an issue with respect to the safety, reliability, performance, or military effectiveness of a nuclear weapon type. .",
      "versionDate": "2025-11-05",
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
        "actionDate": "2025-11-07",
        "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5951",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Nuclear Testing Without Approval Act",
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
        "name": "Congress",
        "updateDate": "2025-11-19T12:21:09Z"
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
      "date": "2025-11-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3106is.xml"
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
      "title": "No Nuclear Testing Without Approval Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T06:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Nuclear Testing Without Approval Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the approval of Congress before explosive nuclear testing may be resumed.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:24Z"
    }
  ]
}
```
