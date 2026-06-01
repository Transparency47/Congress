# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/803?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/803
- Title: Keep Americans Safe Act
- Congress: 119
- Bill type: S
- Bill number: 803
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-12-05T21:26:42Z
- Update date including text: 2025-12-05T21:26:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/803",
    "number": "803",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Keep Americans Safe Act",
    "type": "S",
    "updateDate": "2025-12-05T21:26:42Z",
    "updateDateIncludingText": "2025-12-05T21:26:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T20:42:00Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "DE"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NM"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "VA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-27",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-27",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "RI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "MD"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s803is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 803\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Ms. Hirono (for herself, Mr. Blumenthal , Mr. Coons , Ms. Duckworth , Mr. Durbin , Mr. Heinrich , Mr. Kaine , Mr. King , Ms. Klobuchar , Mr. Markey , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Padilla , Mr. Reed , Ms. Rosen , Mr. Sanders , Ms. Smith , Mr. Van Hollen , Ms. Warren , Mr. Welch , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo regulate large capacity ammunition feeding devices.\n#### 1. Short title\nThis Act may be cited as the Keep Americans Safe Act .\n#### 2. Definitions\nSection 921(a) of title 18, United States Code, is amended by adding at the end the following:\n(38) The term large capacity ammunition feeding device \u2014 (A) means a magazine, belt, drum, feed strip, helical feeding device, or similar device, including any such device joined or coupled with another in any manner, that has an overall capacity of, or that can be readily restored, changed, or converted to accept, more than 10 rounds of ammunition; and (B) does not include an attached tubular device designed to accept, and capable of operating only with, .22 caliber rimfire ammunition. (39) The term qualified law enforcement officer has the meaning given the term in section 926B. .\n#### 3. Restrictions on large capacity ammunition feeding devices\n##### (a) In general\nSection 922 of title 18, United States Code, is amended by inserting after subsection (u) the following:\n(v) (1) It shall be unlawful for a person to import, sell, manufacture, transfer, or possess, in or affecting interstate or foreign commerce, a large capacity ammunition feeding device. (2) Paragraph (1) shall not apply to the possession of any large capacity ammunition feeding device otherwise lawfully possessed on or before the date of enactment of the Keep Americans Safe Act . (3) Paragraph (1) shall not apply to\u2014 (A) the importation for, manufacture for, sale to, transfer to, or possession by the United States or a department or agency of the United States or a State or a department, agency, or political subdivision of a State, or a sale or transfer to or possession by a qualified law enforcement officer employed by the United States or a department or agency of the United States or a State or a department, agency, or political subdivision of a State for purposes of law enforcement (whether on or off-duty), or a sale or transfer to or possession by a campus law enforcement officer for purposes of law enforcement (whether on or off-duty); (B) the importation for, or sale or transfer to a licensee under title I of the Atomic Energy Act of 1954 ( 42 U.S.C. 2011 et seq. ) for purposes of establishing and maintaining an on-site physical protection system and security organization required by Federal law, or possession by an employee or contractor of such licensee on-site for such purposes or off-site for purposes of licensee-authorized training or transportation of nuclear materials; (C) the possession, by an individual who is retired in good standing from service with a law enforcement agency and is not otherwise prohibited from receiving ammunition, of a large capacity ammunition feeding device\u2014 (i) sold or transferred to the individual by the agency upon such retirement; or (ii) that the individual purchased, or otherwise obtained, for official use before such retirement; or (D) the importation, sale, manufacture, transfer, or possession of any large capacity ammunition feeding device by a licensed manufacturer or licensed importer for the purposes of testing or experimentation authorized by the Attorney General. (4) For purposes of paragraph (3)(A), the term campus law enforcement officer means an individual who is\u2014 (A) employed by a private institution of higher education that is eligible for funding under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. ); (B) responsible for the prevention or investigation of crime involving injury to persons or property, including apprehension or detention of persons for such crimes; (C) authorized by Federal, State, or local law to carry a firearm, execute search warrants, and make arrests; and (D) recognized, commissioned, or certified by a government entity as a law enforcement officer. .\n##### (b) Identification markings for large capacity ammunition feeding devices\nSection 923(i) of title 18, United States Code, is amended by adding at the end the following: A large capacity ammunition feeding device manufactured after the date of enactment of the Keep Americans Safe Act shall be identified by a serial number and the date on which the device was manufactured or made, legibly and conspicuously engraved or cast on the device, and such other identification as the Attorney General shall by regulations prescribe. .\n##### (c) Seizure and forfeiture of large capacity ammunition feeding devices\nSection 924(d) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the first sentence\u2014\n**(i)**\nby striking Any firearm or ammunition involved in and inserting Any firearm or ammunition or large capacity ammunition feeding device involved in ;\n**(ii)**\nby striking or (k) and inserting (k), or (v) ; and\n**(iii)**\nby striking any firearm or ammunition intended and inserting any firearm or ammunition or large capacity ammunition feeding device intended ; and\n**(B)**\nby inserting or large capacity ammunition feeding devices after firearms or ammunition each place the term appears;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), by inserting or large capacity ammunition feeding devices after firearms or ammunition ; and\n**(B)**\nin subparagraph (C), by inserting or large capacity ammunition feeding devices after firearms or quantities of ammunition ; and\n**(3)**\nin paragraph (3)(E), by inserting 922(v), after 922(n), .\n#### 4. Penalties\nSection 924(a)(1)(B) of title 18, United States Code, is amended by striking or (q) and inserting (q), or (v) .\n#### 5. Use of Byrne grants for buy-back programs for large capacity ammunition feeding devices\nSection 501(a)(1) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10152(a)(1) ) is amended by adding at the end the following:\n(J) Compensation for surrendered large capacity ammunition feeding devices, as that term is defined in section 921 of title 18, United States Code, under buy-back programs for large capacity ammunition feeding devices. .\n#### 6. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act, the amendments made by this Act, and the application of such provision or amendment to any person or circumstance shall not be affected thereby.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1674",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keep Americans Safe Act",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-09-02T17:50:03Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-09-02T17:50:03Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-09-02T17:50:03Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-09-02T17:50:03Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-09-02T17:50:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-28T15:59:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s803",
          "measure-number": "803",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-06-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s803v00",
            "update-date": "2025-06-10"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Keep Americans Safe Act</b></p> <p>This bill establishes a new criminal offense for the import, sale, manufacture, transfer, or possession of a large capacity ammunition feeding device (LCAFD).</p> <p>The bill does not prohibit certain conduct with respect to an LCAFD, including the following:</p> <ul> <li> importation, sale, manufacture, transfer, or possession related to certain law enforcement efforts, or authorized tests or experiments;</li> <li>importation, sale, transfer, or possession related to securing nuclear materials; and</li> <li> possession by a retired law enforcement officer.</li> </ul> <p>The bill permits continued possession of, but prohibits sale or transfer of, a grandfathered LCAFD.</p> <p>Newly manufactured LCAFDs must display serial number identification and the date of manufacture.</p> <p> Additionally, the bill allows a state or local government to use Edward Byrne Memorial Justice Assistance Grant Program funds to compensate individuals who surrender an LCAFD under a buy-back program.</p>"
        },
        "title": "Keep Americans Safe Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s803.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Keep Americans Safe Act</b></p> <p>This bill establishes a new criminal offense for the import, sale, manufacture, transfer, or possession of a large capacity ammunition feeding device (LCAFD).</p> <p>The bill does not prohibit certain conduct with respect to an LCAFD, including the following:</p> <ul> <li> importation, sale, manufacture, transfer, or possession related to certain law enforcement efforts, or authorized tests or experiments;</li> <li>importation, sale, transfer, or possession related to securing nuclear materials; and</li> <li> possession by a retired law enforcement officer.</li> </ul> <p>The bill permits continued possession of, but prohibits sale or transfer of, a grandfathered LCAFD.</p> <p>Newly manufactured LCAFDs must display serial number identification and the date of manufacture.</p> <p> Additionally, the bill allows a state or local government to use Edward Byrne Memorial Justice Assistance Grant Program funds to compensate individuals who surrender an LCAFD under a buy-back program.</p>",
      "updateDate": "2025-06-10",
      "versionCode": "id119s803"
    },
    "title": "Keep Americans Safe Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Keep Americans Safe Act</b></p> <p>This bill establishes a new criminal offense for the import, sale, manufacture, transfer, or possession of a large capacity ammunition feeding device (LCAFD).</p> <p>The bill does not prohibit certain conduct with respect to an LCAFD, including the following:</p> <ul> <li> importation, sale, manufacture, transfer, or possession related to certain law enforcement efforts, or authorized tests or experiments;</li> <li>importation, sale, transfer, or possession related to securing nuclear materials; and</li> <li> possession by a retired law enforcement officer.</li> </ul> <p>The bill permits continued possession of, but prohibits sale or transfer of, a grandfathered LCAFD.</p> <p>Newly manufactured LCAFDs must display serial number identification and the date of manufacture.</p> <p> Additionally, the bill allows a state or local government to use Edward Byrne Memorial Justice Assistance Grant Program funds to compensate individuals who surrender an LCAFD under a buy-back program.</p>",
      "updateDate": "2025-06-10",
      "versionCode": "id119s803"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s803is.xml"
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
      "title": "Keep Americans Safe Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keep Americans Safe Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to regulate large capacity ammunition feeding devices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T01:48:25Z"
    }
  ]
}
```
