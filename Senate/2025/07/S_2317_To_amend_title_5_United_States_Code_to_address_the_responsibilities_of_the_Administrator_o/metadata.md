# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2317?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2317
- Title: Federal Advisory Committee Database Act
- Congress: 119
- Bill type: S
- Bill number: 2317
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2025-09-08T16:05:48Z
- Update date including text: 2025-09-08T16:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2317",
    "number": "2317",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Federal Advisory Committee Database Act",
    "type": "S",
    "updateDate": "2025-09-08T16:05:48Z",
    "updateDateIncludingText": "2025-09-08T16:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T15:34:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2317is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2317\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Peters (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to address the responsibilities of the Administrator of General Services with respect to Federal advisory committees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Advisory Committee Database Act .\n#### 2. Federal advisory committees\nChapter 10 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 1006\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking The Administrator and inserting the following:\n(1) In general The Administrator ; and\n**(ii)**\nby adding at the end the following:\n(2) Collection of information (A) In general The Committee Management Secretariat established and maintained under paragraph (1) shall continually collect from the head of each agency such information as is necessary for the Administrator to carry out the responsibilities of the Administrator under this section, which shall include, at a minimum, the following with respect to each advisory committee within the jurisdiction of that agency: (i) The name of the advisory committee. (ii) The authority under which the advisory committee is established. (iii) A copy of the charter of the advisory committee. (iv) The interest areas of the advisory committee. (v) The means by which the advisory committee complies with the requirements of section 1004(b)(2) (commonly referred to as a Membership Balance Plan ). (vi) The current (as of the date on which the information is collected) membership of the advisory committee, which shall include, at a minimum, the following with respect to each member of the advisory committee: (I) The name of the member. (II) The ethics designation of the member, such as whether the member is an employee, a special Government employee (as defined in section 202 of title 18), or a representative member. (III) The entity or individual who appointed the member to the advisory committee, which shall include an identification of the authority for that appointment. (IV) The term of the appointment of the member to the advisory committee, as appropriate. (vii) The Advisory Committee Management Officer designated under section 1007(b) with respect to the advisory committee. (viii) The officer or employee designated under section 1009(e) with respect to the advisory committee. (ix) The termination date of the advisory committee, if applicable. (x) With respect to a particular fiscal year, the total operational and staff costs of the advisory committee for that fiscal year, and with respect to the forthcoming fiscal year, the estimated total operational and staff costs of the advisory committee for that forthcoming fiscal year. (xi) The frequency with which the advisory committee (excluding any subcommittee or other subgroup of the advisory committee) has met and the dates on which those meetings have taken place. (xii) A summary of the business conducted at each meeting of the advisory committee. (xiii) The recommendations issued by the advisory committee, which shall include\u2014 (I) the number of those recommendations; and (II) if feasible, information regarding whether those recommendations were partially or fully implemented. (B) Publication The Committee Management Secretariat established and maintained under paragraph (1) shall, with respect to the information collected under subparagraph (A) of this paragraph\u2014 (i) annually publish that information on a public website of the General Services Administration, which shall allow for that information to be downloaded in a format that is machine-readable, as defined in section 3502 of title 44; and (ii) on the website described in clause (i) of this subparagraph, maintain access to that information from previous years, as applicable with respect to relevant records schedules. ;\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nin the matter preceding subparagraph (A), by inserting , in consultation with the head of each agency, after the Administrator ;\n**(II)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (D) and (E), respectively; and\n**(III)**\nby inserting after subparagraph (B) the following:\n(C) whether the committee, for the period covered by the review, complied with the requirements of subsection (a)(2); ; and\n**(ii)**\nby amending paragraph (3) to read as follows:\n(3) Biennial report and recommendations The Administrator shall biennially submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives a report containing the results of the 2 most recent reviews conducted under this subsection, which shall include recommendations to the President and to either the agency head or Congress with respect to action the Administrator believes should be taken. ; and\n**(C)**\nin subsection (c)\u2014\n**(i)**\nin the first sentence\u2014\n**(I)**\nby striking administrative guidelines and management controls and inserting regulations, administrative guidelines, and management controls ; and\n**(II)**\nby inserting after their performance the following: , which shall include guidance regarding how the agency and the advisory committees of the agency should prepare the information that is required to be submitted under subsection (a)(2) to ensure standardization and consistency in the reporting of that information ; and\n**(ii)**\nby adding at the end the following: The Administrator may update the regulations, administrative guidelines, and management controls prescribed under this subsection, as determined necessary by the Administrator. ; and\n**(2)**\nin section 1007\u2014\n**(A)**\nby amending subsection (a) to read as follows:\n(a) Administrative guidelines and management controls Each agency head shall\u2014 (1) establish uniform administrative guidelines and management controls for advisory committees established by that agency, which shall be consistent with directives of the Administrator under sections 1006 and 1009 of this title; (2) maintain systematic information on the nature, functions, and operations of each advisory committee established by that agency; (3) ensure timely and accurate reporting to the Administrator regarding the activities of each advisory committee established by that agency, including with respect to the information required to be submitted under section 1006(a)(2); (4) in coordination with each officer or employee of the Federal Government designated under section 1009(e), establish relevant and appropriate performance measures and outcomes for each advisory committee established by that agency; and (5) ensure that each advisory committee established by that agency, and the staff of each such advisory committee (including each officer or employee of the Federal Government designated under section 1009(e)), complies with the requirements of this chapter and the rules, orders, and regulations promulgated under this chapter. ; and\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (2)\u2014\n**(I)**\nby inserting recommendations, after records, ; and\n**(II)**\nby striking and at the end;\n**(ii)**\nin paragraph (3)\u2014\n**(I)**\nby striking such reports, records, and other papers and inserting the reports, records, recommendations, and other papers described in paragraph (2) ; and\n**(II)**\nby striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(4) serve as the primary liaison between the agency and the Administrator. .\n#### 3. No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act or the amendments made by this Act.",
      "versionDate": "2025-07-17",
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
            "name": "Advisory bodies",
            "updateDate": "2025-08-20T17:57:50Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-20T17:57:50Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-20T17:57:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-08T16:05:48Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2317is.xml"
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
      "title": "Federal Advisory Committee Database Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T06:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Advisory Committee Database Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to address the responsibilities of the Administrator of General Services with respect to Federal advisory committees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:21Z"
    }
  ]
}
```
