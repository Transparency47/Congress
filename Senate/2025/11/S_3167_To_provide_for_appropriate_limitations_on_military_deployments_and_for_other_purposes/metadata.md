# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3167?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3167
- Title: No Troops in Our Streets Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3167
- Origin chamber: Senate
- Introduced date: 2025-11-07
- Update date: 2025-11-25T19:11:14Z
- Update date including text: 2025-11-25T19:11:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in Senate
- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-07: Introduced in Senate

## Actions

- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3167",
    "number": "3167",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001208",
        "district": "",
        "firstName": "Elissa",
        "fullName": "Sen. Slotkin, Elissa [D-MI]",
        "lastName": "Slotkin",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "No Troops in Our Streets Act of 2025",
    "type": "S",
    "updateDate": "2025-11-25T19:11:14Z",
    "updateDateIncludingText": "2025-11-25T19:11:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-07",
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
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T23:09:01Z",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "AZ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "IL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3167is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3167\nIN THE SENATE OF THE UNITED STATES\nNovember 7, 2025 Ms. Slotkin (for herself, Mr. Kelly , Ms. Duckworth , Mr. Blumenthal , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide for appropriate limitations on military deployments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Troops in Our Streets Act of 2025 .\n#### 2. Termination authority for posse comitatus exceptions\nSection 1385 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever and inserting (a) In general .\u2014Whoever ; and\n**(2)**\nby adding at the end the following new subsections:\n(b) Congressional authority To terminate Congress may terminate any exception to subsection (a) at any time by enacting a joint resolution of disapproval as described under subsection (c). (c) Joint resolution of disapproval (1) In general In this subsection, the term joint resolution of disapproval means only a joint resolution of either House of Congress\u2014 (A) the title of which is as follows: A joint resolution expressing congressional disapproval of the deployment of Armed Forces in [_____]. , with the blank space being filled with the location prohibited; and (B) the sole matter after the resolving clause of which is the following: Congress prohibits the deployment of Armed Forces under title [___], United States Code, with respect to [_____] in [_____] for [____]. , with the first blank space being filled with the title under which authority to send troops was provided, the second blank space being filled with a short description of the military actions prohibited, the third blank space being filled with the location where the deployment is prohibited, and the fourth blank space being filled with the duration of the prohibition. (2) Introduction A joint resolution of disapproval may be introduced\u2014 (A) in the Senate, by the majority leader (or the majority leader\u2019s designee) or the minority leader (or the minority leader\u2019s designee); and (B) in the House of Representatives, by the Speaker of the House or the minority leader. (3) Consideration in the Senate (A) Committee referral A joint resolution of disapproval introduced in the Senate shall be referred to the Committee on Armed Services of the Senate. (B) Reporting and discharge If the Committee on Armed Services of the Senate has not reported a joint resolution of disapproval within 5 calendar days after the date of referral of the joint resolution, that committee shall be discharged from further consideration of the joint resolution and the joint resolution shall be placed on the appropriate calendar. (C) Proceeding to consideration Notwithstanding Rule XXII of the Standing Rules of the Senate, it is in order at any time after the Committee on Armed Services reports a joint resolution of disapproval to the Senate or has been discharged from consideration of such a joint resolution (even though a previous motion to the same effect has been disagreed to) to move to proceed to the consideration of the joint resolution, and all points of order against the joint resolution (and against consideration of the joint resolution) are waived. The motion to proceed is not debatable. The motion is not subject to a motion to postpone. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order. (D) Rulings of the chair on procedure Appeals from the decisions of the Chair relating to the application of the rules of the Senate, as the case may be, to the procedure relating to a joint resolution of disapproval shall be decided without debate. (E) Consideration of veto messages Debate in the Senate of any veto message with respect to a joint resolution of disapproval, including all debatable motions and appeals in connection with the joint resolution, shall be limited to 10 hours, to be equally divided between, and controlled by, the Majority Leader and the Minority Leader or their designees. (F) Floor consideration in the House of Representatives If a committee of the House of Representatives to which a joint resolution of disapproval has been referred has not reported the joint resolution within 5 calendar days after the date of referral, that committee shall be discharged from further consideration of the joint resolution. (4) Rules relating to the Senate and the House of Representatives (A) Treatment of House of Representatives joint resolution in Senate (i) Receipt before passage of Senate resolution If, before the passage by the Senate of a joint resolution of disapproval, the Senate receives an identical joint resolution from the House of Representatives, the following procedures shall apply: (I) That joint resolution shall not be referred to a committee. (II) With respect to that joint resolution\u2014 (aa) the procedure in the Senate shall be the same as if no joint resolution had been received from the House of Representatives; but (bb) the vote on passage shall be on the joint resolution from the House of Representatives. (ii) Receipt following passage of Senate resolution If, following passage of a joint resolution of disapproval in the Senate, the Senate receives an identical joint resolution from the House of Representatives, that joint resolution shall be placed on the appropriate Senate calendar. (iii) No companion resolution If a joint resolution of disapproval is received from the House of Representatives, and no companion joint resolution has been introduced in the Senate, the Senate procedures under this subparagraph shall apply to the House of Representatives joint resolution. (B) Treatment of Senate joint resolution in House of Representatives In the House of Representatives, the following procedures shall apply to a joint resolution of disapproval received from the Senate (unless the House of Representatives has already passed a joint resolution relating to the same proposed action): (i) The joint resolution shall be referred to the Committee on Armed Services of the House of Representatives. (ii) If the Committee on Armed Services of the House of Representatives has not reported the joint resolution within two calendar days after the date of referral, that committee shall be discharged from further consideration of the joint resolution. (iii) Beginning on the third legislative day after the Committee on Armed Services of the House of Representatives reports the joint resolution to the House of Representatives or has been discharged from further consideration thereof, it shall be in order to move to proceed to consider the joint resolution in the House of Representatives. All points of order against the motion are waived. Such a motion shall not be in order after the House of Representatives has disposed of a motion to proceed on the joint resolution. The previous question shall be considered as ordered on the motion to its adoption without intervening motion. The motion shall not be debatable. A motion to reconsider the vote by which the motion is disposed of shall not be in order. (iv) The joint resolution shall be considered as read. All points of order against the joint resolution and against its consideration are waived. The previous question shall be considered as ordered on the joint resolution to final passage without intervening motion except two hours of debate equally divided and controlled by the sponsor of the joint resolution (or a designee) and an opponent. A motion to reconsider the vote on passage of the joint resolution shall not be in order. (C) Inapplicability to revenue measure in House of Representatives The provisions of this paragraph shall not apply in the House of Representatives to a joint resolution of disapproval that is a revenue measure. (D) Rules of Senate and House of Representatives This paragraph is enacted by Congress\u2014 (i) as an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, and supersedes other rules only to the extent that it is inconsistent with such rules; and (ii) with full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House. (5) Congressional intent If a joint resolution of disapproval with respect to the deployment of the Armed Forces in a particular location is not introduced or enacted, no court or agency may infer any intent of Congress from any action or inaction of Congress with regard to such joint resolution of disapproval. (d) Severability If any provision of this section, or any application of such provision to any person or circumstance, is held to be unconstitutional, the remainder of this section and the application of this section to any other person or circumstance shall not be affected. .\n#### 3. Termination authority for section 12406 activations\nSection 12406 of title 10, United States Code, is amended\u2014\n**(1)**\nby striking Whenever\u2014 and inserting (a) In general .\u2014Whenever ; and\n**(2)**\nby adding at the end the following new subsections:\n(b) Congressional authority To terminate Congress may terminate any activation pursuant to subsection (a) at any time by enacting a joint resolution of disapproval. (c) Joint resolution of disapproval In this section, the term joint resolution of disapproval has the meanings given such term under subsection (c) of section 1385 of title 18. (d) Severability If any provision of this section, or any application of such provision to any person or circumstance, is held to be unconstitutional, the remainder of this section and the application of this section to any other person or circumstance shall not be affected. .\n#### 4. Funding for State and local law enforcement\n##### (a) In general\nIn addition to amounts otherwise appropriated, out of any money in the Treasury not otherwise appropriated, for fiscal year 2026, for Department of Justice\u2014State and Local Law Enforcement Activities\u2014Office of Justice Programs\u2014State and Local Law Enforcement Assistance , there is appropriated\u2014\n**(1)**\n$600,000,000, to remain available until expended, for the Edward Byrne Memorial Justice Assistance Grant program as authorized by subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ) (except that section 1001(c), and the special rules for Puerto Rico under section 505(g), of title I of that Act shall not apply for purposes of this Act);\n**(2)**\n$150,000,000, to remain available until expended, for a community violence intervention and prevention initiative; and\n**(3)**\n$50,000,000, to remain available until expended, for emergency law enforcement assistance, as authorized by section 609M of the Justice Assistance Act of 1984 ( 34 U.S.C. 50101 ), to support any of the purposes specified in section 501 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10152 ), of which the President may direct not greater than $10,000,000 per law enforcement emergency, as defined in section 609N of the Justice Assistance Act of 1984 ( 34 U.S.C. 50102 ), with the approval of the chief executive of the State and locality, to support State and local law enforcement.\n##### (b) Community-Oriented policing hiring\nIn addition to amounts otherwise appropriated, out of any money in the Treasury not otherwise appropriated, for fiscal year 2026, there is appropriated $100,000,000, to remain available until expended, for grants for the hiring and rehiring of additional career law enforcement officers under section 1701 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ).\n##### (c) Prohibition\nNone of the amounts made available under this section may be used to fund the assignment of Federal law enforcement personnel to States and localities.\n##### (d) Emergency designation\nAmounts appropriated under subsections (a) and (b) are designated by Congress as an emergency requirement pursuant to section 4001(a)(1) of S. Con. Res. 14 (117th Congress), the concurrent resolution on the budget for fiscal year 2022, and to legislation establishing fiscal year 2026 budget enforcement in the House of Representatives.",
      "versionDate": "2025-11-07",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-25T19:11:14Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3167is.xml"
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
      "title": "No Troops in Our Streets Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Troops in Our Streets Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for appropriate limitations on military deployments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:28Z"
    }
  ]
}
```
