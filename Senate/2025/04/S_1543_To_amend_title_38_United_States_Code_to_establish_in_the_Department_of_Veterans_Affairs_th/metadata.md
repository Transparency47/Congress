# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1543?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1543
- Title: Veterans Opportunity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1543
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2026-03-19T11:03:26Z
- Update date including text: 2026-03-19T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1543",
    "number": "1543",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Veterans Opportunity Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:26Z",
    "updateDateIncludingText": "2026-03-19T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
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
        "item": [
          {
            "date": "2025-05-21T20:00:36Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:36Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-04-30T23:28:52Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NH"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NV"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1543is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1543\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Banks (for himself, Ms. Hassan , Mr. Scott of Florida , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to establish in the Department of Veterans Affairs the Veterans Economic Opportunity and Transition Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Opportunity Act of 2025 .\n#### 2. Establishment of Veterans Economic Opportunity and Transition Administration\n##### (a) Veterans Economic Opportunity and Transition Administration\n**(1) In general**\nPart V of title 38, United States Code, is amended by adding at the end the following new chapter:\n80 Veterans Economic Opportunity and Transition Administration Sec. 8001. Organization of Administration. 8002. Functions of Administration. 8003. Annual report to Congress. 8001. Organization of Administration (a) Veterans Economic Opportunity and Transition Administration (1) There is in the Department a Veterans Economic Opportunity and Transition Administration. (2) The primary function of the Veterans Economic Opportunity and Transition Administration is the administration of the programs of the Department that provide assistance related to economic opportunity to veterans and their dependents and survivors. (b) Under Secretary for Economic Opportunity and Transition The Veterans Economic Opportunity and Transition Administration is under the Under Secretary for Veterans Economic Opportunity and Transition, who is directly responsible to the Secretary for the operations of the Administration. 8002. Functions of Administration The Veterans Economic Opportunity and Transition Administration is responsible for the administration of the following: (1) Vocational rehabilitation and employment programs. (2) Educational assistance programs. (3) Veterans\u2019 housing loan and related programs. (4) The responsibilities of the Secretary with respect to the Transition Assistance Program under section 1144 of title 10. (5) Any other program of the Department that the Secretary determines appropriate. 8003. Annual report to Congress (a) In general The Secretary shall include in the annual report to the Congress required by section 529 of this title a report on the programs administered by the Under Secretary for Veterans Economic Opportunity and Transition. (b) Contents Each report under subsection (a) shall include the following with respect to each program described in such subsection during the fiscal year covered by that report: (1) The number of claims received. (2) The number of claims decided. (3) The average processing time for a claim. (4) The number of successful outcomes (as determined by the Secretary). (5) The number of full-time equivalent employees. (6) The amounts expended for information technology. .\n**(2) Clerical amendments**\nThe tables of chapters at the beginning of title 38, United States Code, and of part V of title 38, United States Code, are each amended by inserting after the item relating to chapter 79 the following new item:\n80. Veterans Economic Opportunity and Transition Administration 8001 .\n##### (b) Effective date\nChapter 80 of title 38, United States Code, as added by subsection (a), shall take effect on October 1 of the first fiscal year commencing after the date of the enactment of this Act.\n##### (c) Labor rights\nAny labor rights, inclusion in the bargaining unit, and collective bargaining agreement that affects an employee of the Department of Veterans Affairs who is transferred to the Veterans Economic Opportunity and Transition Administration, as established under chapter 80 of title 38, United States Code, as added by subsection (a), shall apply in the same manner to such employee after such transfer.\n##### (d) Sense of Congress\nIt is the sense of Congress that the creation of the Veterans Economic Opportunity and Transition Administration and the transfer of functions to such Administration from the Veterans Benefits Administration should not, directly or indirectly\u2014\n**(1)**\ncause the budget or spending of the Department of Veterans Affairs to increase or decrease relative to the budget or level of spending of the Department in effect on the day before the date of the enactment of this Act; or\n**(2)**\nserve as a basis or justification for any increase or decrease in the number of full-time equivalent employees of the Department.\n#### 3. Under Secretary for Veterans Economic Opportunity and Transition\n##### (a) Under Secretary\n**(1) In general**\nChapter 3 of title 38, United States Code, is amended by inserting after section 306 the following new section:\n306A. Under Secretary for Veterans Economic Opportunity and Transition (a) Under Secretary (1) There is in the Department an Under Secretary for Veterans Economic Opportunity and Transition, who is appointed by the President, by and with the advice and consent of the Senate. (2) The Under Secretary for Veterans Economic Opportunity and Transition shall be appointed without regard to political affiliation or activity and solely on the basis of demonstrated ability in\u2014 (A) the administration of programs within the Veterans Economic Opportunity and Transition Administration or programs of similar content and scope; and (B) information technology. (b) Responsibilities The Under Secretary for Veterans Economic Opportunity and Transition is the head of, and is directly responsible to the Secretary for the operations of, the Veterans Economic Opportunity and Transition Administration. (c) Vacancies (1) Whenever a vacancy in the position of Under Secretary for Veterans Economic Opportunity and Transition occurs or is anticipated, the Secretary shall establish a commission to recommend individuals to the President for appointment to the position. (2) A commission established under this subsection shall be composed of the following members appointed by the Secretary: (A) Three persons representing education and training, vocational rehabilitation, employment, real estate, mortgage finance and related industries, and survivor benefits activities affected by the Veterans Economic Opportunity and Transition Administration. (B) Two persons representing veterans served by the Veterans Economic Opportunity and Transition Administration. (C) Two persons who have experience in the management of private sector benefits programs of similar content and scope to the economic opportunity and transition programs of the Department. (D) The Deputy Secretary of Veterans Affairs. (E) The chairman of the Veterans\u2019 Advisory Committee on Education formed under section 3692 of this title. (F) One person who has held the position of Under Secretary for Veterans Economic Opportunity and Transition, if the Secretary determines that it is desirable for such person to be a member of the commission. (3) A commission established under this subsection shall recommend at least three individuals for appointment to the position of Under Secretary for Veterans Economic Opportunity and Transition. The commission shall submit all recommendations to the Secretary. The Secretary shall forward the recommendations to the President and the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives with any comments the Secretary considers appropriate. Thereafter, the President may request the commission to recommend additional individuals for appointment. (4) The Assistant Secretary or Deputy Assistant Secretary of Veterans Affairs who performs personnel management and labor relations functions shall serve as the executive secretary of a commission established under this subsection. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 306 the following new item:\n306A. Under Secretary for Veterans Economic Opportunity and Transition. .\n##### (b) Conforming amendments\nTitle 38, United States Code, is further amended\u2014\n**(1)**\nin section 306(c)(2), by striking subparagraphs (A) and (E) and redesignating subparagraphs (B), (C), (D), and (F), as subparagraphs (A) through (D), respectively;\n**(2)**\nin section 317(d)(2), by inserting after Under Secretary for Benefits, the following: the Under Secretary for Veterans Economic Opportunity and Transition, ;\n**(3)**\nin section 318(d)(2), by inserting after Under Secretary for Benefits, the following: the Under Secretary for Veterans Economic Opportunity and Transition, ;\n**(4)**\nin section 516(e)(2)(C), by striking Health and the Under Secretary for Benefits and inserting Health, the Under Secretary for Benefits, and the Under Secretary for Veterans Economic Opportunity and Transition ;\n**(5)**\nin section 541(a)(2)(B), by striking Health and the Under Secretary for Benefits and inserting Health, the Under Secretary for Benefits, and the Under Secretary for Veterans Economic Opportunity and Transition ;\n**(6)**\nin section 542(a)(2)(B)(iii), by striking Health and the Under Secretary for Benefits and inserting Health, the Under Secretary for Benefits, and the Under Secretary for Veterans Economic Opportunity and Transition ;\n**(7)**\nin section 544(a)(2)(B)(vi), by striking Health and the Under Secretary for Benefits and inserting Health, the Under Secretary for Benefits, and the Under Secretary for Veterans Economic Opportunity and Transition ;\n**(8)**\nin section 709(c)(2)(A), by inserting after Under Secretary for Benefits, the following: the Under Secretary for Veterans Economic Opportunity and Transition, ;\n**(9)**\nin section 7701(a), by inserting after assistance the following: , other than assistance related to Economic Opportunity and Transition, ; and\n**(10)**\nin section 7703, by striking paragraphs (2) and (3) and redesignating paragraphs (4) and (5) as paragraphs (2) and (3), respectively.\n##### (c) Effective date\nSection 306A of title 38, United States Code, as added by subsection (a), and the amendments made by this section, shall take effect on October 1, 2025.\n#### 4. Transfer of services\n##### (a) Report to Congress\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the progress toward establishing the Veterans Economic Opportunity and Transition Administration, as established under section 8001 of title 38, United States Code, as added by section 2, and the transition of the provision of services to veterans by such Administration.\n##### (b) Certification\nThe Secretary of Veterans Affairs may not transfer the function of providing any services to veterans to the Veterans Economic Opportunity and Transition Administration, as established under section 8001 of title 38, United States Code, as added by section 2, until the Secretary submits to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives certification that\u2014\n**(1)**\nthe transition of the provision of services to such Administration will not negatively affect the provision of such services to veterans; and\n**(2)**\nsuch services are ready to be transferred.\n##### (c) Deadline for certification\nThe Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives the certification required by subsection (b)\u2014\n**(1)**\nno earlier than April 1 of the first fiscal year commencing after the date of the enactment of this Act; and\n**(2)**\nno later than September 1 of the first fiscal year commencing after the date of the enactment of this Act.\n##### (d) Failure To certify\nIf the Secretary fails to submit the certification required by subsection (b) by the date specified in subsection (c)(2), the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report that includes\u2014\n**(1)**\nthe reason why the certification was not made by such date; and\n**(2)**\nthe estimated date when the certification will be made.",
      "versionDate": "2025-04-30",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-06-05T14:21:33Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-06-05T14:21:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T20:59:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
    "originChamber": "Senate",
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
          "measure-id": "id119s1543",
          "measure-number": "1543",
          "measure-type": "s",
          "orig-publish-date": "2025-04-30",
          "originChamber": "SENATE",
          "update-date": "2025-07-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1543v00",
            "update-date": "2025-07-03"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans Opportunity Act of 2025</strong></p><p>This bill establishes the Veterans Economic Opportunity and Transition Administration to administer economic opportunity assistance programs for veterans and their dependents and survivors.</p><p>Specifically, the Veterans Economic Opportunity and Transition Administration must administer the following Department of Veterans Affairs (VA) programs:</p><ul><li>vocational rehabilitation and employment programs,</li><li>educational assistance programs,</li><li>veterans' housing loan and related programs,</li><li>the responsibilities of the VA with respect to the\u00a0Transition Assistance Program, and</li><li>any other VA program that the VA determines is\u00a0appropriate.</li></ul><p>Prior to the transfer of administrative responsibilities, the bill requires the VA to certify that (1) the transition of the provision of services will not negatively affect the provision of such services to veterans, and (2) such services are ready to be transferred.</p>"
        },
        "title": "Veterans Opportunity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1543.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Opportunity Act of 2025</strong></p><p>This bill establishes the Veterans Economic Opportunity and Transition Administration to administer economic opportunity assistance programs for veterans and their dependents and survivors.</p><p>Specifically, the Veterans Economic Opportunity and Transition Administration must administer the following Department of Veterans Affairs (VA) programs:</p><ul><li>vocational rehabilitation and employment programs,</li><li>educational assistance programs,</li><li>veterans' housing loan and related programs,</li><li>the responsibilities of the VA with respect to the\u00a0Transition Assistance Program, and</li><li>any other VA program that the VA determines is\u00a0appropriate.</li></ul><p>Prior to the transfer of administrative responsibilities, the bill requires the VA to certify that (1) the transition of the provision of services will not negatively affect the provision of such services to veterans, and (2) such services are ready to be transferred.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119s1543"
    },
    "title": "Veterans Opportunity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Opportunity Act of 2025</strong></p><p>This bill establishes the Veterans Economic Opportunity and Transition Administration to administer economic opportunity assistance programs for veterans and their dependents and survivors.</p><p>Specifically, the Veterans Economic Opportunity and Transition Administration must administer the following Department of Veterans Affairs (VA) programs:</p><ul><li>vocational rehabilitation and employment programs,</li><li>educational assistance programs,</li><li>veterans' housing loan and related programs,</li><li>the responsibilities of the VA with respect to the\u00a0Transition Assistance Program, and</li><li>any other VA program that the VA determines is\u00a0appropriate.</li></ul><p>Prior to the transfer of administrative responsibilities, the bill requires the VA to certify that (1) the transition of the provision of services will not negatively affect the provision of such services to veterans, and (2) such services are ready to be transferred.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119s1543"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1543is.xml"
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
      "title": "Veterans Opportunity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Opportunity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to establish in the Department of Veterans Affairs the Veterans Economic Opportunity and Transition Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:52Z"
    }
  ]
}
```
