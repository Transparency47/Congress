# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3655?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3655
- Title: Hong Kong Economic and Trade Office (HKETO) Certification Act
- Congress: 119
- Bill type: S
- Bill number: 3655
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-03-20T11:03:19Z
- Update date including text: 2026-03-20T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3655",
    "number": "3655",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Hong Kong Economic and Trade Office (HKETO) Certification Act",
    "type": "S",
    "updateDate": "2026-03-20T11:03:19Z",
    "updateDateIncludingText": "2026-03-20T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T16:06:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "AK"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "UT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "VA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3655is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3655\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. Merkley (for himself, Mr. Sullivan , Mr. Curtis , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require the President to remove the extension of certain privileges, exemptions, and immunities to the Hong Kong Economic and Trade Offices if Hong Kong no longer enjoys a high degree of autonomy from the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hong Kong Economic and Trade Office (HKETO) Certification Act .\n#### 2. Determination on whether to extend certain privileges, exemptions, and immunities to the Hong Kong Economic and Trade Offices in the United States\n##### (a) Determination required\nNot later than 30 days after the date of the enactment of this Act, and thereafter as part of each certification required by the Secretary of State under section 205(a)(1)(A) of the United States-Hong Kong Policy Act of 1992 ( 22 U.S.C. 5725(a)(1)(A) ), the Secretary of State shall, as part of such certification, include a separate determination that\u2014\n**(1)**\nthe Hong Kong Economic and Trade Offices\u2014\n**(A)**\nmerit extension and application of the privileges, exemptions, and immunities specified in subsection (b); or\n**(B)**\nno longer merit extension and application of the privileges, exemptions, and immunities specified in subsection (b); and\n**(2)**\na detailed report justifying that determination, which may include considerations related to United States national security interests.\n##### (b) Privileges, exemptions, and immunities specified\nThe privileges, exemptions, and immunities specified in this subsection are the privileges, exemptions, and immunities extended and applied to the Hong Kong Economic and Trade Offices under section 1 of the Act entitled An Act to extend certain privileges, exemptions, and immunities to Hong Kong Economic and Trade Offices , approved June 27, 1997 ( 22 U.S.C. 288k ).\n##### (c) Effect of determination\n**(1) Termination**\nIf the Secretary of State determines under subsection (a)(1)(B) that the Hong Kong Economic and Trade Offices no longer merit extension and application of the privileges, exemptions, and immunities specified in subsection (b), the Hong Kong Economic and Trade Offices shall terminate operations not later than 180 days after the date on which that determination is delivered to the appropriate congressional committees, as part of the certification required under section 205(a)(1)(A) of the United States-Hong Kong Policy Act of 1992 ( 22 U.S.C. 5725(a)(1)(A) ).\n**(2) Continued operations**\nIf the Secretary of State determines under subsection (a)(1)(A) that the Hong Kong Economic and Trade Offices merit extension and application of the privileges, exemptions, and immunities specified in subsection (b), the Hong Kong Economic and Trade Offices may continue operations for the one-year period following the date of the certification under section 205(a)(1)(A) of the United States-Hong Kong Policy Act of 1992 ( 22 U.S.C. 5725(a)(1)(A) ) that includes that determination or until the next certification required under such section is submitted, whichever occurs first, unless a disapproval resolution is enacted under subsection (d).\n##### (d) Congressional review\n**(1) Disapproval resolution**\nIn this subsection, the term disapproval resolution means only a joint resolution of either House of Congress\u2014\n**(A)**\nthe title of which is the following: A joint resolution disapproving the determination by the Secretary of State that the Hong Kong Economic and Trade Offices continue to merit extension and application of certain privileges, exemptions, and immunities. ; and\n**(B)**\nthe sole matter after the resolving clause of which is the following: Congress disapproves of the determination by the Secretary of State under section 2(a)(1)(A) of the Hong Kong Economic and Trade Office (HKETO) Certification Act that the Hong Kong Economic and Trade Offices merit extension and application of certain privileges, exemptions, and immunities, on ___. , with the blank space being filled with the appropriate date.\n**(2) Introduction**\nA disapproval resolution may be introduced\u2014\n**(A)**\nin the House of Representatives, by the majority leader or the minority leader; and\n**(B)**\nin the Senate, by the majority leader (or the majority leader\u2019s designee) or the minority leader (or the minority leader\u2019s designee).\n**(3) Floor consideration in house of representatives**\nIf a committee of the House of Representatives to which a disapproval resolution has been referred has not reported the resolution within 10 legislative days after the date of referral, that committee shall be discharged from further consideration of the resolution.\n**(4) Consideration in senate**\n**(A) Committee referral**\nA disapproval resolution introduced in the Senate shall be referred to the Committee on Foreign Relations.\n**(B) Reporting and discharge**\nIf the Committee on Foreign Relations of the Senate has not reported a disapproval resolution within 10 legislative days after the date of referral of the resolution, that committee shall be discharged from further consideration of the resolution and the resolution shall be placed on the appropriate calendar.\n**(C) Proceeding to consideration**\nNotwithstanding Rule XXII of the Standing Rules of the Senate, it is in order at any time after the Committee on Foreign Relations reports a disapproval resolution to the Senate or has been discharged from consideration of such a resolution (even though a previous motion to the same effect has been disagreed to) to move to proceed to the consideration of the resolution, and all points of order against the resolution (and against consideration of the resolution) are waived. The motion to proceed is not debatable. The motion is not subject to a motion to postpone. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order.\n**(D) Rulings of the chair on procedure**\nAppeals from the decisions of the Chair relating to the application of the rules of the Senate, as the case may be, to the procedure relating to a disapproval resolution shall be decided without debate.\n**(E) Consideration of veto messages**\nDebate in the Senate of any veto message with respect to a disapproval resolution, including all debatable motions and appeals in connection with the resolution, shall be limited to 10 hours, to be equally divided between, and controlled by, the majority leader and the minority leader or their designees.\n**(5) Rules relating to senate and house of representatives**\n**(A) Treatment of senate resolution in house**\nIn the House of Representatives, the following procedures shall apply to a disapproval resolution received from the Senate (unless the House has already passed a resolution relating to the same proposed action):\n**(i)**\nThe resolution shall be referred to the appropriate committees.\n**(ii)**\nIf a committee to which a resolution has been referred has not reported the resolution within 10 legislative days after the date of referral, that committee shall be discharged from further consideration of the resolution.\n**(iii)**\nBeginning on the third legislative day after each committee to which a resolution has been referred reports the resolution to the House or has been discharged from further consideration thereof, it shall be in order to move to proceed to consider the resolution in the House. All points of order against the motion are waived. Such a motion shall not be in order after the House has disposed of a motion to proceed on the resolution. The previous question shall be considered as ordered on the motion to its adoption without intervening motion. The motion shall not be debatable. A motion to reconsider the vote by which the motion is disposed of shall not be in order.\n**(iv)**\nThe resolution shall be considered as read. All points of order against the resolution and against its consideration are waived. The previous question shall be considered as ordered on the resolution to final passage without intervening motion except 2 hours of debate equally divided and controlled by the offeror of the motion to proceed (or a designee) and an opponent. A motion to reconsider the vote on passage of the resolution shall not be in order.\n**(B) Treatment of house resolution in senate**\n**(i) Received before passage of senate resolution**\nIf, before the passage by the Senate of a disapproval resolution, the Senate receives an identical resolution from the House of Representatives, the following procedures shall apply:\n**(I)**\nThat resolution shall not be referred to a committee.\n**(II)**\nWith respect to that resolution\u2014\n**(aa)**\nthe procedure in the Senate shall be the same as if no resolution had been received from the House of Representatives; but\n**(bb)**\nthe vote on passage shall be on the resolution from the House of Representatives.\n**(ii) Received after passage of senate resolution**\nIf, following passage of a disapproval resolution in the Senate, the Senate receives an identical resolution from the House of Representatives, that resolution shall be placed on the appropriate Senate calendar.\n**(iii) No senate companion**\nIf a disapproval resolution is received from the House of Representatives, and no companion resolution has been introduced in the Senate, the Senate procedures under this subsection shall apply to the resolution from the House of Representatives.\n**(C) Application to revenue measures**\nThe provisions of this paragraph shall not apply in the House of Representatives to a disapproval resolution that is a revenue measure.\n**(6) Rules of house of representatives and senate**\nThis subsection is enacted by Congress\u2014\n**(A)**\nas an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, and supersedes other rules only to the extent that it is inconsistent with such rules; and\n**(B)**\nwith full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.\n##### (e) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives.\n**(2) Hong Kong Economic and Trade Offices**\nThe term Hong Kong Economic and Trade Offices has the meaning given that term in section 1(c) of the Act entitled An Act to extend certain privileges, exemptions, and immunities to Hong Kong Economic and Trade Offices , approved June 27, 1997 ( 22 U.S.C. 288k ).\n#### 3. Limitation on contracting relating to Hong Kong Economic and Trade Offices\n##### (a) In general\nOn and after the date of the enactment of this Act, an entity of the United States Government may enter into an agreement or partnership with the Hong Kong Economic and Trade Offices to promote tourism, culture, business, or other matters relating to Hong Kong only if\u2014\n**(1)**\nthe Secretary of State has submitted to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives a determination under section 2(a)(1)(A) that the Hong Kong Economic and Trade Offices merit extension and application of certain privileges, exemptions, and immunities;\n**(2)**\na disapproval resolution under section 2(d) is not enacted during the 90-day period following the submission of that determination; and\n**(3)**\nthe agreement or partnership does not promote efforts by the Government of the Hong Kong Special Administrative Region and the Government of the People\u2019s Republic of China\u2014\n**(A)**\nto justify the dismantling of the autonomy of Hong Kong and the freedoms and rule of law guaranteed by the Sino-British Joint Declaration of 1984; and\n**(B)**\nto portray within the United States the Government of the Hong Kong Special Administrative Region or the Government of the People\u2019s Republic of China as protecting the rule of law or the human rights and civil liberties of the people of Hong Kong.\n##### (b) Hong Kong Economic and Trade Offices defined\nIn this section, the term Hong Kong Economic and Trade Offices has the meaning given that term in section 1(c) of the Act entitled An Act to extend certain privileges, exemptions, and immunities to Hong Kong Economic and Trade Offices , approved June 27, 1997 ( 22 U.S.C. 288k ).\n#### 4. Policy of United States on promotion of autonomy of Government of the Hong Kong Special Administrative Region\nIt is the policy of the United States\u2014\n**(1)**\nto ensure that entities of the United States Government do not knowingly assist in the promotion of Hong Kong as a free and autonomous city or the Government of the Hong Kong Special Administrative Region as committed to protecting the human rights of the people of Hong Kong or fully maintaining the rule of law required for human rights and economic prosperity as long as the Secretary of State continues to determine under section 205(a)(1) of the United States-Hong Kong Policy Act of 1992 ( 22 U.S.C. 5725(a)(1) ) that Hong Kong does not enjoy a high degree of autonomy from the People\u2019s Republic of China and does not warrant treatment under the laws of the United States in the same manner as those laws were applied to Hong Kong before July 1, 1997;\n**(2)**\nto recognize that promotion of Hong Kong as described in paragraph (1) should be considered propaganda for the efforts of the People\u2019s Republic of China to dismantle rights and freedom guaranteed to the residents of Hong Kong by the International Covenant on Civil and Political Rights and the Sino-British Joint Declaration of 1984;\n**(3)**\nto ensure that entities of the United States Government do not engage in or assist with propaganda of the People\u2019s Republic of China regarding Hong Kong; and\n**(4)**\nto engage with the Government of the Hong Kong Special Administrative Region, through all relevant entities of the United States Government, seeking the release of political prisoners, the end of arbitrary detentions, the resumption of a free press and fair and free elections open to all candidates, and the restoration of an independent judiciary.",
      "versionDate": "2026-01-15",
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
        "actionDate": "2025-04-07",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2661",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Hong Kong Economic and Trade Office (HKETO) Certification Act",
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
        "name": "International Affairs",
        "updateDate": "2026-02-11T14:25:58Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3655is.xml"
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
      "title": "Hong Kong Economic and Trade Office (HKETO) Certification Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hong Kong Economic and Trade Office (HKETO) Certification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the President to remove the extension of certain privileges, exemptions, and immunities to the Hong Kong Economic and Trade Offices if Hong Kong no longer enjoys a high degree of autonomy from the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T04:18:20Z"
    }
  ]
}
```
