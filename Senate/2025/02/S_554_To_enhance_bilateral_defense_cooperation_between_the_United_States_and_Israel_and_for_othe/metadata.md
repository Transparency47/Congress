# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/554?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/554
- Title: United States-Israel Defense Partnership Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 554
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2026-01-11T23:14:56Z
- Update date including text: 2026-01-11T23:14:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/554",
    "number": "554",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "United States-Israel Defense Partnership Act of 2025",
    "type": "S",
    "updateDate": "2026-01-11T23:14:56Z",
    "updateDateIncludingText": "2026-01-11T23:14:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T21:49:12Z",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "MI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NE"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NV"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "NC"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "VA"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "MO"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "IN"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "IA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "UT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "AZ"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "VA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "GA"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "OR"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NV"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "ND"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "OK"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "ME"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "WV"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NJ"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TN"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "AK"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "ID"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "TX"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "SD"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "OK"
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s554is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 554\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Sullivan (for himself, Mr. Peters , Mr. Blumenthal , Mr. Ricketts , and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo enhance bilateral defense cooperation between the United States and Israel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States-Israel Defense Partnership Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe United States and Israel\u2014\n**(A)**\nare bound closely by historic and cultural ties and mutual interests; and\n**(B)**\nface common threats, which are constantly evolving in scope, scale, and lethality;\n**(2)**\nto most effectively counter such shared threats, the United States and Israel must expand their defense partnership to develop new technologies and leverage the unique capabilities offered by defense industrial base of each country; and\n**(3)**\nthis Act furthers such goal through the establishment of several joint initiatives.\n#### 3. United States-Israel program on countering unmanned systems\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nThe increasing use of unmanned systems by state and nonstate actors poses a significant threat to the national security of the United States and its allies, including Israel.\n**(2)**\nCooperation in developing and deploying counter-unmanned systems technology will enhance mutual security and strengthen bilateral defense capabilities.\n**(3)**\nIsrael is a global leader in the development of advanced counter-unmanned systems technologies, and a cooperative program will leverage shared expertise and resources to address evolving threats.\n##### (b) Establishment\n**(1) In general**\nThe Secretary of Defense, with the concurrence of the Minister of Defense of Israel, shall establish a cooperative program between the United States and Israel, to be known as the United States-Israel Counter-Unmanned Systems Program , for the purpose of enhancing cooperation between the United States and Israel for purposes of\u2014\n**(A)**\ndeveloping, testing, evaluating, and deploying advanced technologies for countering unmanned systems that threaten the United States and Israel;\n**(B)**\nsharing technical expertise and data on emerging unmanned systems and related threats;\n**(C)**\nconducting joint research and development initiatives; and\n**(D)**\ndeploying and integrating counter-unmanned systems for mutual defense.\n**(2) Activities**\nThe program established under this subsection shall include the following:\n**(A)**\nCollaborative research initiatives involving government, private sector, and academic institutions in the United States and Israel, conducted in a manner that protects sensitive technology and information and the national security interests of the United States and Israel.\n**(B)**\nJoint training exercises and information-sharing mechanisms to enhance operational readiness of personnel of the United States and of Israel.\n**(C)**\nThe establishment, within the Department of Defense, of a United States-Israel Counter-Unmanned Systems Program Office to oversee program execution and coordination.\n**(D)**\nThe procurement and deployment of counter-unmanned systems.\n##### (c) Annual report\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter, the Secretary of Defense shall submit to the Committee on Armed Services of the Senate and the Committee on Armed Services of the House of Representatives a report on the implementation of the program established under this section.\n**(2) Elements**\nEach report required by paragraph (1) shall include, for the preceding year\u2014\n**(A)**\na description of activities conducted under the program;\n**(B)**\nan assessment of progress made in addressing unmanned systems threats and requirements;\n**(C)**\nan assessment of the program\u2019s collaboration with other relevant United States Government programs, including the United States-Israel Operations-Technology Working Group and Counter Unmanned Aerial Systems program run by the Irregular Warfare Technical Support Directorate; and\n**(D)**\nrecommendations for future program activities and funding.\n**(3) Form**\nEach report submitted under paragraph (1) shall be submitted in unclassified form but may include a classified annex as necessary to protect sensitive information.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated $150,000,000 for each of fiscal years 2026 through 2030 to carry out the program under this section.\n##### (e) Rule of construction\nNothing in this section shall be construed to alter or supersede agreements or obligations between the United States and Israel in existence on the date of the enactment of this Act.\n#### 4. Extension and modification of United States-Israel anti-tunnel cooperation\nSection 1279 of the National Defense Authorization Act for Fiscal Year 2016 ( Public Law 114\u201392 ; 22 U.S.C. 8606 note) is amended\u2014\n**(1)**\nin subsection (b)(4), by striking $50,000,000 and inserting $80,000,000 ; and\n**(2)**\nin subsection (f), by striking December 31, 2026 and inserting December 31, 2028 .\n#### 5. Extension and modification of United States-Israel cooperation to counter unmanned aerial systems\nSection 1278 of the National Defense Authorization Act for Fiscal Year 2020 ( 22 U.S.C. 8606 note) is amended\u2014\n**(1)**\nin subsection (b)(4), by striking $55,000,000 and inserting $75,000,000 ; and\n**(2)**\nin subsection (f), by striking December 31, 2026 and inserting December 31, 2028 .\n#### 6. United States-Israel emerging technology capabilities cooperation\n##### (a) Statement of policy\nIt is the policy of the United States to support and encourage further defense collaboration with Israel in areas of emerging technologies capable of enabling the warfare capabilities of both the United States and Israel to meet emerging defense challenges, including in the areas of artificial intelligence, cybersecurity, robotics, quantum, and automation.\n##### (b) Authority To establish emerging defense technology capabilities program with Israel\n**(1) In general**\nThe Secretary of Defense, upon request by the Ministry of Defense of Israel and in consultation with the Secretary of State and the Director of National Intelligence, is authorized to carry out, jointly with Israel, research, development, test, and evaluation in areas of emerging technologies capable of enabling the warfare capabilities of the United States and Israel to meet emerging defense challenges, including in the areas of artificial intelligence, cybersecurity, robotics, quantum, and automation.\n**(2) Protection of sensitive information**\nAny activity carried out pursuant to the authority provided by paragraph (1) shall be conducted in a manner that appropriately protects sensitive information and the national security interests of the United States and Israel.\n**(3) Report**\nNone of the activities described in paragraph (1) may be carried out until the date on which the Secretary of Defense submits to the Committees on Armed Services of the Senate and the House of Representatives a report that sets forth the following:\n**(A)**\nA memorandum of agreement between the United States and Israel regarding sharing of research and development costs for the capabilities described in paragraph (1), and any supporting documents.\n**(B)**\nA certification that such memorandum of agreement\u2014\n**(i)**\nrequires sharing of costs of projects, including in-kind support, between the United States and Israel;\n**(ii)**\nestablishes a framework to negotiate the rights to any intellectual property developed under the memorandum of agreement; and\n**(iii)**\nrequires the United States Government to receive semiannual reports on expenditure of funds, if any, by the Government of Israel, including a description of what the funds have been used for, when funds were expended, and an identification of entities that expended the funds.\n##### (c) Lead agency\nNot earlier than the date on which the Secretary of Defense submits the report required by subsection (b)(3), the Secretary of Defense shall designate the Irregular Warfare Technology Support Directorate as the lead agency of the Department of Defense in carrying out this section.\n##### (d) Semiannual reports\nThe Secretary of Defense shall submit to the appropriate committees of Congress on a semiannual basis a report that contains a copy of the most recent semiannual report provided by the Government of Israel to the Department of Defense pursuant to subsection (b)(3)(B)(iii).\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated $50,000,000 for each of fiscal years 2026 through 2030 to carry out the program under this section.\n#### 7. Extension of War Reserves Stockpile authority\nSection 12001(d) of the Department of Defense Appropriations Act, 2005 ( Public Law 108\u2013287 ; 118 Stat. 1011) is amended by striking after January 1, 2027 and inserting after January 1 2029 .\n#### 8. Establishment of Defense Innovation Unit office in Israel\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall establish in Israel a Defense Innovation Unit office\u2014\n**(1)**\nto engage the Minister of Defense of Israel and representatives of the private sector in collaborative efforts to counter development by Iran of dual-use defense technologies; and\n**(2)**\nto leverage resources and innovation activities of the United States and Israel for the benefit of the national security of the United States and Israel.\n#### 9. National Technology Industrial Base\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Defense shall seek to engage the Minister of Defense of Israel in a discussion of the process of the ascension of Israel into the national technology and industrial base (as defined in section 4801 of title 10, United States Code).\n##### (b) Protection of sensitive information\nAny activity carried out pursuant to the authority provided by subsection (a) shall be conducted in a manner that appropriately protects sensitive information and the national security interests of the United States and Israel.\n#### 10. Assessment of integrated air and missile defense in region covered by United States Central Command\n##### (a) Assessment required\nThe Secretary of Defense shall conduct an assessment of the integrated air and missile defense in the region cover by United States Central Command.\n##### (b) Elements\nThe assessment conducted pursuant to subsection (a) shall cover the following:\n**(1)**\nThe current strength of the integrated air and missile defense in the region described in subsection (a).\n**(2)**\nHow best to strengthen the integrated air and missile defense described in paragraph (1).\n**(3)**\nWhat would be required to expand or deepen cooperation among the United States, Israel, and other regional partners of the United States to achieve full operational capability of the integrated air and missile defense described in paragraph (1), including identification of the amount of funding and new legal authorities that may be required for such expansion or deepening.\n##### (c) Considerations\nIn carrying out the assessment required by subsection (a), the Secretary shall consider the following:\n**(1)**\nThe strategy required by section 1658(b) of James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( Public Law 117\u2013263 ).\n**(2)**\nCurrent cooperation among partners of the United States in the region described by subsection (a) on integrated air and missile defense.\n**(3)**\nLessons learned in countering the April 13, 2024, and October 1, 2024, airstrikes by Iran against Israel.\n##### (d) Report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall submit to the Committees on Armed Services of the Senate and the House of Representatives a report on the assessment conducted under this section.\n**(2) Form**\nThe report required by paragraph (1) shall be submitted in unclassified form but may contain a classified annex.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-02-12",
        "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1229",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "United States-Israel Defense Partnership Act of 2025",
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
        "updateDate": "2025-05-07T14:28:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119s554",
          "measure-number": "554",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2026-01-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s554v00",
            "update-date": "2026-01-11"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>United States-Israel Defense Partnership Act of 2025</strong></p><p>This bill requires or authorizes certain actions to increase defense-related cooperation between the United States and Israel.</p><p>Specifically, the bill requires the Department of Defense (DOD) to</p><ul><li>establish a cooperative program, with the concurrence of Israel's Ministry of Defense (MOD),\u00a0to develop and deploy advanced technologies for countering unmanned systems that threaten the United States and Israel;</li><li>establish in Israel an office\u00a0of the Defense Innovation Unit (an organization that\u00a0focuses on rapidly fielding and scaling commercial technology across the U.S. military); and</li><li>seek to engage Israel's MOD on the ascension of Israel into the national technology and industrial base (currently\u00a0defined in law as the persons and organizations engaged in research, development, production, integration, services, or information technology activities conducted within the United States, the United Kingdom, Australia, New Zealand, and Canada).</li></ul><p>The bill authorizes\u00a0DOD, upon request of Israel's MOD, to jointly conduct research, development, test, and evaluation (RDT&E) of emerging technologies such as artificial intelligence and robotics\u00a0to meet defense challenges.</p><p>Additionally, the bill extends the authority for DOD to (1)\u00a0carry out\u00a0RDT&E on a joint basis with Israel to establish anti-tunnel and counter unmanned aerial systems capabilities through 2028, and (2)\u00a0transfer defense articles intended for use as reserve stocks for Israel through January 1, 2029.</p>"
        },
        "title": "United States-Israel Defense Partnership Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s554.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>United States-Israel Defense Partnership Act of 2025</strong></p><p>This bill requires or authorizes certain actions to increase defense-related cooperation between the United States and Israel.</p><p>Specifically, the bill requires the Department of Defense (DOD) to</p><ul><li>establish a cooperative program, with the concurrence of Israel's Ministry of Defense (MOD),\u00a0to develop and deploy advanced technologies for countering unmanned systems that threaten the United States and Israel;</li><li>establish in Israel an office\u00a0of the Defense Innovation Unit (an organization that\u00a0focuses on rapidly fielding and scaling commercial technology across the U.S. military); and</li><li>seek to engage Israel's MOD on the ascension of Israel into the national technology and industrial base (currently\u00a0defined in law as the persons and organizations engaged in research, development, production, integration, services, or information technology activities conducted within the United States, the United Kingdom, Australia, New Zealand, and Canada).</li></ul><p>The bill authorizes\u00a0DOD, upon request of Israel's MOD, to jointly conduct research, development, test, and evaluation (RDT&E) of emerging technologies such as artificial intelligence and robotics\u00a0to meet defense challenges.</p><p>Additionally, the bill extends the authority for DOD to (1)\u00a0carry out\u00a0RDT&E on a joint basis with Israel to establish anti-tunnel and counter unmanned aerial systems capabilities through 2028, and (2)\u00a0transfer defense articles intended for use as reserve stocks for Israel through January 1, 2029.</p>",
      "updateDate": "2026-01-11",
      "versionCode": "id119s554"
    },
    "title": "United States-Israel Defense Partnership Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>United States-Israel Defense Partnership Act of 2025</strong></p><p>This bill requires or authorizes certain actions to increase defense-related cooperation between the United States and Israel.</p><p>Specifically, the bill requires the Department of Defense (DOD) to</p><ul><li>establish a cooperative program, with the concurrence of Israel's Ministry of Defense (MOD),\u00a0to develop and deploy advanced technologies for countering unmanned systems that threaten the United States and Israel;</li><li>establish in Israel an office\u00a0of the Defense Innovation Unit (an organization that\u00a0focuses on rapidly fielding and scaling commercial technology across the U.S. military); and</li><li>seek to engage Israel's MOD on the ascension of Israel into the national technology and industrial base (currently\u00a0defined in law as the persons and organizations engaged in research, development, production, integration, services, or information technology activities conducted within the United States, the United Kingdom, Australia, New Zealand, and Canada).</li></ul><p>The bill authorizes\u00a0DOD, upon request of Israel's MOD, to jointly conduct research, development, test, and evaluation (RDT&E) of emerging technologies such as artificial intelligence and robotics\u00a0to meet defense challenges.</p><p>Additionally, the bill extends the authority for DOD to (1)\u00a0carry out\u00a0RDT&E on a joint basis with Israel to establish anti-tunnel and counter unmanned aerial systems capabilities through 2028, and (2)\u00a0transfer defense articles intended for use as reserve stocks for Israel through January 1, 2029.</p>",
      "updateDate": "2026-01-11",
      "versionCode": "id119s554"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s554is.xml"
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
      "title": "United States-Israel Defense Partnership Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "United States-Israel Defense Partnership Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enhance bilateral defense cooperation between the United States and Israel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:34Z"
    }
  ]
}
```
