# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/167?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/167
- Title: A bill to amend title 18, United States Code, to punish criminal offenses targeting law enforcement officers, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 167
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2026-02-06T11:56:28Z
- Update date including text: 2026-02-06T11:56:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/167",
    "number": "167",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "A bill to amend title 18, United States Code, to punish criminal offenses targeting law enforcement officers, and for other purposes.",
    "type": "S",
    "updateDate": "2026-02-06T11:56:28Z",
    "updateDateIncludingText": "2026-02-06T11:56:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
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
            "date": "2025-01-21T21:14:07Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-21T21:14:07Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ID"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NE"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ID"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "KS"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "WV"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AL"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NE"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "PA"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "SC"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "FL"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "ME"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "SC"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "OH"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "MS"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "IN"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "ND"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MT"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "WV"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "NC"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "LA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "OK"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "IN"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s167is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 167\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mr. Tillis introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to punish criminal offenses targeting law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect and Serve Act of 2025 .\n#### 2. Crimes targeting law enforcement officers\n##### (a) In general\nChapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Crimes targeting law enforcement officers (a) In general Whoever, in any circumstance described in subsection (b), knowingly assaults a law enforcement officer causing serious bodily injury, or attempts to do so\u2014 (1) shall be imprisoned not more than 10 years, fined in accordance with this title, or both; and (2) shall be imprisoned for any term of years or for life, fined in accordance with this title, or both, if\u2014 (A) death results from the offense; or (B) the offense includes kidnapping or an attempt to kidnap, or an attempt to kill. (b) Circumstances described For purposes of subsection (a), the circumstances described in this subsection are that\u2014 (1) the conduct described in subsection (a) occurs during the course of, or as the result of, the travel of the defendant or the victim\u2014 (A) across a State line or national border; or (B) using a channel, facility, or instrumentality of interstate or foreign commerce; (2) the defendant uses a channel, facility, or instrumentality of interstate or foreign commerce in connection with the conduct described in subsection (a); (3) in connection with the conduct described in subsection (a), the defendant employs a firearm, dangerous weapon, explosive or incendiary device, or other weapon that has traveled in interstate or foreign commerce; (4) the conduct described in subsection (a)\u2014 (A) interferes with commercial or other economic activity in which the victim is engaged at the time of the conduct; or (B) otherwise affects interstate or foreign commerce; or (5) the victim is a Federal law enforcement officer. (c) Certification requirement (1) In general No prosecution of any offense described in this section may be undertaken by the United States, except under the certification in writing of the Attorney General, or a designee, that\u2014 (A) the State does not have jurisdiction; (B) the State has requested that the Federal Government assume jurisdiction; (C) the verdict or sentence obtained pursuant to State charges left demonstratively unvindicated the Federal interest in protecting the public safety; or (D) a prosecution by the United States is in the public interest and necessary to secure substantial justice. (2) Rule of construction Nothing in this subsection shall be construed to limit the authority of Federal officers, or a Federal grand jury, to investigate possible violations of this section. (d) Definitions In this section: (1) Law enforcement officer The term law enforcement officer means an employee of a governmental or public agency who is authorized by law\u2014 (A) to engage in or supervise the prevention, detection, or the investigation of any criminal violation of law; or (B) to engage in or supervise the detention or the incarceration of any person for any criminal violation of law. (2) State The term State means a State of the United States, the District of Columbia, or any commonwealth, territory, or possession of the United States. .\n##### (b) Clerical amendment\nThe table of sections for chapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Crimes targeting law enforcement officers. .",
      "versionDate": "2025-01-21",
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
        "actionDate": "2025-02-25",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1551",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect and Serve Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2025-03-03T18:07:58Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-03-03T18:07:58Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-03-03T18:07:58Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-03-03T18:07:58Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-03-03T18:07:58Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-03-03T18:07:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-24T20:10:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119s167",
          "measure-number": "167",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s167v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protect and Serve Act of 2025</strong></p><p>This bill establishes a new criminal offense for knowingly assaulting a law enforcement officer and causing serious bodily injury (or attempting to do so) in circumstances that affect interstate commerce.</p><p>It imposes criminal penalties\u2014a prison term, a fine, or both\u2014on a violator.</p>"
        },
        "title": "Protect and Serve Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s167.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect and Serve Act of 2025</strong></p><p>This bill establishes a new criminal offense for knowingly assaulting a law enforcement officer and causing serious bodily injury (or attempting to do so) in circumstances that affect interstate commerce.</p><p>It imposes criminal penalties\u2014a prison term, a fine, or both\u2014on a violator.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s167"
    },
    "title": "Protect and Serve Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect and Serve Act of 2025</strong></p><p>This bill establishes a new criminal offense for knowingly assaulting a law enforcement officer and causing serious bodily injury (or attempting to do so) in circumstances that affect interstate commerce.</p><p>It imposes criminal penalties\u2014a prison term, a fine, or both\u2014on a violator.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s167"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s167is.xml"
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
      "title": "Protect and Serve Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect and Serve Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to punish criminal offenses targeting law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:33:48Z"
    }
  ]
}
```
