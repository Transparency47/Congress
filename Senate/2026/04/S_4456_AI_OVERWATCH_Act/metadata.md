# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4456?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4456
- Title: AI OVERWATCH Act
- Congress: 119
- Bill type: S
- Bill number: 4456
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-12T22:16:15Z
- Update date including text: 2026-05-12T22:16:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4456",
    "number": "4456",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
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
    "title": "AI OVERWATCH Act",
    "type": "S",
    "updateDate": "2026-05-12T22:16:15Z",
    "updateDateIncludingText": "2026-05-12T22:16:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T17:12:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MA"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "AR"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NH"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4456is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4456\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Banks (for himself, Ms. Warren , Mr. Cotton , Mrs. Shaheen , Mr. Ricketts , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Under Secretary of Commerce for Industry and Security to require a license for the export, reexport, or in-country transfer of certain integrated circuits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Artificial Intelligence Oversight of Verified Exports and Restrictions on Weaponizable Advanced Technology to Covered High-Risk Actors Act or the AI OVERWATCH Act .\n#### 2. License requirement for exports of covered integrated circuits to countries of concern\nPart I of the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 et seq. ) is amended by inserting after section 1758 the following:\n1758A. Control of exports of covered integrated circuits (a) Definitions In this section: (1) Allied country The term allied country means any country listed in Country Group A under Supplement No. 1 to part 740 of the Export Administration Regulations (as in effect on January 1, 2026). (2) Appropriate congressional committees The term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate. (3) Commerce Control List The term Commerce Control List means the list set forth in Supplement No. 1 to part 774 of the Export Administration Regulations. (4) Country of concern The term country of concern means\u2014 (A) the People\u2019s Republic of China, including the Hong Kong and Macau Special Administrative Regions; (B) the Republic of Cuba; (C) the Islamic Republic of Iran; (D) the Democratic People\u2019s Republic of Korea; (E) the Russian Federation; and (F) any other foreign country listed in Country Group D:5 under Supplement No. 1 to part 740 of the Export Administration Regulations, as published on January 1, 2026, that is designated by the Secretary of State as a country of concern for purposes of this section and for which notice of such designation has been published in the Federal Register. (5) Covered agency heads The term covered agency heads means the Secretary of Defense, the Secretary of Energy, the Secretary of State, and the Director of the White House Office of Science and Technology Policy. (6) Covered integrated circuit (A) In general Subject to subparagraphs (B), (C), and (D), the term covered integrated circuit means\u2014 (i) an integrated circuit, computer, or other product\u2014 (I) classified under Export Control Classification Number 3A090 or 4A090 or related Export Control Classification Numbers; or (II) that is functionally equivalent or substantially similar to a circuit, computer, or product described in subclause (I), including certain similar products listed under Export Control Classification Number 5A002.z; or (ii) an integrated circuit that has 1 or more digital processing units with\u2014 (I) a total processing performance of 4,800 or more; (II) a total processing performance of 2,400 or more and a performance density of 1.6 or more; (III) a total processing performance of 1,600 or more and a performance density of 3.2 or more; or (IV) a total DRAM bandwidth of 1,400 gigabytes per second or more, interconnect bandwidth of 1,100 gigabytes per second or more, or a sum of DRAM bandwidth and interconnect bandwidth of 1,700 gigabytes per second or more. (B) Authority to update technical parameters Beginning 24 months after the date of the submission to Congress of the American Artificial Intelligence Victory Strategy required in subsection (f), the Under Secretary of Commerce for Industry and Security may add or modify technical parameters for the definition of covered integrated circuit for purposes of this section though notice in the Federal Register, so long as\u2014 (i) the addition or modification poses no adverse impact on the national security of the United States; (ii) not fewer than 30 days before the addition or modification takes effect, the Secretary of Commerce\u2014 (I) consults with the appropriate congressional committees regarding such addition or modification; and (II) in conjunction with each agency that is part of the Operating Committee for Export Policy and in coordination with the Director of National Intelligence, updates the American Artificial Intelligence Victory Strategy required in subsection (f) and submits such update to the appropriate congressional committees; and (iii) the Operating Committee for Export Policy has approved the addition or modification by majority vote. (C) Products included Except as provided in subparagraph (D), the term covered integrated circuit includes a product containing such a covered integrated circuit. (D) Exclusion The term covered integrated circuit does not include\u2014 (i) covered integrated circuits or products containing a covered integrated circuit that are not designed or marketed for use in a data center; or (ii) microprocessor microcircuits, such as central processing units, that are not graphics processing units or similar products. (7) Operating Committee for Export Policy The term Operating Committee for Export Policy means the Operating Committee for Export Policy referred to in section 1763(c) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( 50 U.S.C. 4822(c) ). (8) Performance density; total processing performance The terms performance density and total processing performance have the meanings given those terms in, and are calculated as provided for under, Export Control Classification Number 3A090 in the Commerce Control List (as in effect on January 1, 2026). (9) Restricted integrated circuit (A) In general Subject to subparagraphs (B), (C), and (D), the term restricted integrated circuit means a covered integrated circuit that is\u2014 (i) an integrated circuit that has 1 or more digital processing units\u2014 (I) with a total processing performance of 21,000 or more; or (II) with a total processing performance of 1,600 or more and a performance density of 21 or more; or (ii) an integrated circuit that was first marketed for sale after January 1, 2026, and that has 1 or more digital processing units with\u2014 (I) a total processing performance of 4,800 or more; (II) a total processing performance of 2,400 or more and a performance density of 1.6 or more; or (III) a total processing performance of 1,600 or more and a performance density of 3.2 or more. (B) Authority to update technical parameters The Under Secretary of Commerce for Industry and Security may add or modify technical parameters for the definition of restricted integrated circuit in the same manner and subject to the same restrictions as the authority described in paragraph (6)(B). (C) Products included Except as provided by subparagraph (D), the term restricted integrated circuit includes a product containing such a restricted integrated circuit. (D) Exclusion The term restricted integrated circuit does not include\u2014 (i) restricted integrated circuits or products containing a restricted integrated circuit that are not designed or marketed for use in a data center; or (ii) microprocessor microcircuits, such as central processing units, that are not graphics processing units or similar products. (10) Trusted United States person The term trusted United States person means any United States person designated as a trusted United States person pursuant to subsection (h)(2). (b) License requirement (1) In general Beginning on the date of the enactment of this section, the Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall require a license for the export, reexport, or in-country transfer of a covered integrated circuit or a restricted integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern. (2) General license prohibited The Under Secretary of Commerce for Industry and Security may not issue a general license for the purpose of fulfilling the license requirement in paragraph (1). (c) Certification to Congress (1) Certification requirement Not fewer than 30 days prior to approving any license for the export, reexport, or in-country transfer of a covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern, the Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall submit to the appropriate congressional committees a copy of the license application and proposed license, including\u2014 (A) the quantity of covered integrated circuit, identified by an Export Control Classification Number, as applicable, and by technical parameters of the covered integrated circuit; (B) the ultimate consignee or end-user of the covered integrated circuit; (C) any and all license conditions; (D) a certification that the export, reexport, or in-country transfer of the covered integrated circuit has verifiable and enforceable mechanisms for ensuring the ultimate consignee or end-user has not, does not, and will not support or enable, directly or indirectly, the military, intelligence, surveillance, or cyber-enabled capabilities of a country of concern, including\u2014 (i) that the United States Government has no information indicating that the ultimate consignee or end-user has, does, or will support or enable, directly or indirectly, the military, intelligence, surveillance, or cyber-enabled capabilities of a country of concern; (ii) an explanation of how the license conditions support the certification; and (iii) in the case that the license concerns a country of concern that engages in a military-civil fusion policy or maintains a law that requires persons to provide support and assistance to national security bodies, public security bodies, or relevant military bodies of the country of concern, details on how the license conditions address the specific threats arising from such policy or law; (E) a certification that approving the license will not adversely impact the defense industrial base of the United States, including the availability of covered integrated circuits for United States persons, including all of the major subcomponents of the covered integrated circuits, such as high-bandwidth memory; (F) a certification that approving the license will not adversely impact the technology leadership and advantage of the United States in total nationally installed processing power capacity relative to the country of concern related to the ultimate consignee or end user of the covered integrated circuit; (G) a certification that approving the license will not adversely impact the national security of the United States; (H) the underlying analyses supporting the certifications required in subparagraphs (D), (E), (F), and (G); and (I) a technical assessment (including an alternative assessment by the Director of National Intelligence, if applicable) of how the export, reexport, or in-country transfer of the covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern affects the artificial intelligence leadership of the United States, including in terms of global market share, in artificial intelligence models, artificial intelligence cloud services, and covered integrated circuits, respectively. (2) Extension of review period for certain submissions In the case that a submission to Congress under paragraph (1) is submitted on a date that is on or after July 10 and on or before September 7 in any year, paragraph (1) shall apply by substituting 60 days for 30 days . (3) Limitation The license described in subsection (b) may not be issued until the date that is not fewer than 30 days after the committees described in paragraph (1) received the certification required in such paragraph. (d) Termination of licenses Any license issued or approved prior to the date of the enactment of this section for the export, reexport, or in-country transfer of a covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern is terminated. (e) Temporary prohibition The Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall deny all licenses for the export, reexport, or in-country transfer of a covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern, within one business day of receiving any application for such a license, until the date that is 14 days after the submission to Congress of the American Artificial Intelligence Victory Strategy required in subsection (f). (f) American Artificial Intelligence Victory Strategy The Secretary of Commerce, in conjunction with the covered agency heads and in coordination with the Director of National Intelligence, shall submit to the appropriate congressional committees an American Artificial Intelligence Victory Strategy that details\u2014 (1) a whole-of-government framework to win the artificial intelligence race; (2) the national security and economic implications of the People\u2019s Republic of China winning the artificial intelligence race; (3) the effect that access by countries of concern to covered integrated circuits, semiconductor manufacturing equipment, and related subcomponents that are from the United States or allied countries would have on the artificial intelligence race, the capabilities of the People\u2019s Republic of China, and United States national security; (4) recommendations for policy changes the United States Government should make to best position the United States in the artificial intelligence race against the People\u2019s Republic of China; (5) an assessment of the implications of the export, reexport, or in-country transfer of covered integrated circuits to countries of concern for the military, intelligence, surveillance, or cyber-enabled capabilities of such countries; and (6) an assessment of the covered integrated circuit production numbers and capabilities of the People\u2019s Republic of China for fiscal years 2026 and 2027, including\u2014 (A) a determination of whether the People\u2019s Republic of China would cease or reduce its efforts to pursue indigenous production and use of Chinese-designed and manufactured covered integrated circuits if entities located or headquartered in, or the ultimate parent company of which is headquartered in, the People\u2019s Republic of China are provided access to covered integrated circuits designed in the United States; (B) a comparison of the covered integrated circuit production numbers and capabilities of the People\u2019s Republic of China to the covered integrated circuit production numbers and capabilities of the United States and allies of the United States; and (C) a quantitative analysis, to the extent feasible, examining the artificial intelligence capabilities of countries of concern if such countries relied solely on indigenous production of covered integrated circuits using indigenously produced manufacturing equipment and related subcomponents. (g) License prohibition for restricted integrated circuits The Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall deny all licenses for the export, reexport, or in-country transfer of a restricted integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern. (h) Exemption from certain license requirements for trusted United States persons (1) In general The requirement for a license under sections 742.6 and 744.23 of the Export Administration Regulations shall not apply to the export, reexport, or in-country transfer of a covered integrated circuit if the covered integrated circuit\u2014 (A) is not destined for Macau, Hong Kong, or a country listed in Country Group D:5 under Supplement No. 1 to part 740 of the Export Administration Regulations; and (B) will remain under the ownership and control of a trusted United States person or a subsidiary of a trusted United States person once the covered integrated circuit is in operation. (2) Implementation Not later than 90 days after the date of the enactment of this section, the Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall\u2014 (A) seek input from the public regarding the standards and requirements a United States person should be required to meet to obtain a designation as a trusted United States person; (B) based on such input, prescribe regulations establishing such standards and requirements, which shall include\u2014 (i) establishment by the United States person of reasonable security standards, including physical security, cybersecurity, remote access, secure covered integrated circuit repair and disposal procedures, and other measures designed to prevent the illicit transfer, diversion, or access to covered integrated circuits; (ii) a requirement that the United States person may not transfer or install a majority of its aggregate total processing performance of covered integrated circuits outside the United States; (iii) a requirement that not more than an aggregate 10 percent of the ultimate beneficial ownership of the United States person may be held, directly or indirectly, by any entity that primarily resides, is domiciled, or conducts the majority of its business in a country of concern; (iv) robust know-your-customer standards; (v) a preference for sourcing advanced integrated circuits and subcomponents from production facilities that support the revival of semiconductor manufacturing in the United States; and (vi) annual audit or attestation requirements to ensure compliance with clauses (i), (ii), (iii), and (iv); and (C) prescribe regulations establishing the process by which the Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall approve such a designation. (3) Expansion to allied countries The Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall consider options for securely expanding the license exemption program described in this subsection to certain allied countries. .",
      "versionDate": "2026-04-30",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-05-12T22:16:14Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4456is.xml"
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
      "title": "AI OVERWATCH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AI OVERWATCH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Artificial Intelligence Oversight of Verified Exports and Restrictions on Weaponizable Advanced Technology to Covered High-Risk Actors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Under Secretary of Commerce for Industry and Security to require a license for the export, reexport, or in-country transfer of certain integrated circuits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:31Z"
    }
  ]
}
```
