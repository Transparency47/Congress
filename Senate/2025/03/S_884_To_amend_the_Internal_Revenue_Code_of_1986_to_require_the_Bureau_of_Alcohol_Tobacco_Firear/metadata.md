# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/884?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/884
- Title: ATF Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 884
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2025-11-21T12:03:19Z
- Update date including text: 2025-11-21T12:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/884",
    "number": "884",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "ATF Transparency Act",
    "type": "S",
    "updateDate": "2025-11-21T12:03:19Z",
    "updateDateIncludingText": "2025-11-21T12:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T17:45:47Z",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "MT"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "OK"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "ID"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "MS"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "WY"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "MT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "KS"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s884is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 884\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Risch (for himself, Mr. Daines , Mr. Lankford , Mr. Crapo , Mrs. Hyde-Smith , Ms. Lummis , Mr. Sheehy , and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Internal Revenue Code of 1986 to require the Bureau of Alcohol, Tobacco, Firearms, and Explosives to establish an administrative relief process for individuals whose applications for transfer and registration of a firearm were denied, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ATF Transparency Act .\n#### 2. Administrative relief for denial of firearm transfer application\n##### (a) In general\nSection 5812 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(c) Administrative relief (1) In general With respect to any application described in subsection (a) for the transfer and registration of a firearm which is denied by the Secretary based on a determination that transferring the firearm to the transferee would violate subsection (d) of section 922 of title 18, United States Code, or receipt of the firearm by the transferee would violate subsection (g) or (n) of that section or State, local, or tribal law, the Secretary shall\u2014 (A) provide the transferee with the relevant NICS transaction number with respect to such application, (B) permit such transferee to appeal such denial to the Secretary in a manner similar to the process for appeals provided under section 25.10 of title 28, Code of Federal Regulations, and (C) permit such transferee to provide information to the Secretary to prevent any subsequent erroneous denial or extended delay by NICS pursuant to a program (as established by the Secretary) similar to the Voluntary Appeal File program described in section 25.10(g) of title 28, Code of Federal Regulations. (2) Attorney fees In the case of any successful appeal by the transferee pursuant to the process described in paragraph (1)(B), the Secretary shall reimburse the transferee for any reasonable and necessary attorney fees incurred with respect to such appeal. (3) NICS For purposes of this subsection, the term NICS means the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ). .\n##### (b) Effective date\nThe amendment made by this section shall apply to applications for the transfer and registration of a firearm which are filed or pending on or after the date of enactment of this Act.\n#### 3. Timely processing of applications\n##### (a) Transfer of firearms\nSection 5812 of the Internal Revenue Code of 1986, as amended by section 2, is amended by adding at the end the following new subsection:\n(d) Processing of applications (1) In general Notwithstanding subsection (a), if an application described in such subsection with respect to the transfer and registration of a firearm has been filed with the Secretary and the Secretary fails to make a determination regarding whether to approve or deny such application prior to the date which is 3 business days after the date on which such application was originally filed by the transferor, the transfer and registration of such firearm to the transferee shall be deemed to have been approved by the Secretary for purposes of this section and such transfer may be made. The Secretary shall only deny an application described in subsection (a) on the grounds that the applicable requirements under such subsection have not been satisfied, and may not deny an application solely on the grounds that a determination regarding whether to approve or deny such application could not be completed by the Secretary during the period described in the preceding sentence. (2) Safe harbor (A) In general In the case of an application described in subsection (a) which, following the expiration of the 3-day period under paragraph (1), has been deemed to have been approved by the Secretary for purposes of this section and for which the transfer of the firearm has been made, if the Secretary subsequently determines that the applicable requirements under such subsection have not been satisfied and that such application should have been denied, the Secretary shall provide actual notice of such determination to the transferor and transferee of such firearm. (B) Criminal liability In the case of a determination described in subparagraph (A) that an application for transfer and registration of a firearm should have been denied\u2014 (i) the transferor may not be held liable for any violation of subsection (d) of section 922 of title 18, United States Code, and (ii) the transferee may not be held liable for any violation of subsection (g) or (n) of section 922 of title 18, United States Code, provided that the transferee returns the firearm to the Secretary within the 14-day period subsequent to the date on which the transferee received notice from the Secretary regarding such determination. .\n##### (b) Making of firearms\nSection 5822 of the Internal Revenue Code of 1986 is amended by adding at the end the following: Notwithstanding the preceding sentences, if a person files an application to make and register a firearm with the Secretary and the Secretary fails to make a determination regarding whether to approve or deny such application prior to the date which is 3 business days after the date on which such application was originally filed by such person, such application shall be deemed to have been approved by the Secretary for purposes of this section and such firearm may be made by such person. The Secretary shall only deny an application to make and register a firearm on the grounds that the applicable requirements under this section have not been satisfied, and may not deny an application solely on the grounds that a determination regarding whether to approve or deny such application could not be completed by the Secretary during the period described in the preceding sentence. .\n##### (c) Effective date\nThe amendments made by this section shall apply to applications which are filed or pending on or after the date of enactment of this Act.\n#### 4. Reports and agreements\n##### (a) Unresolved NICS checks\nNot later than 180 days after the date of enactment of this Act, the Comptroller General of the United States, in conjunction with the Inspector General of the Department of Justice, shall submit a report to Congress\u2014\n**(1)**\ndetailing the number of NICS inquiries received during the period of calendar years 2010 through 2024 with respect to the transfer of a firearm which remained unresolved following the expiration of the 90-day period described in section 25.9(b)(1) of title 28, Code of Federal Regulations; and\n**(2)**\nproviding recommendations for administrative actions to be adopted by the Bureau of Alcohol, Tobacco, Firearms, and Explosives to minimize the number of unresolved NICS inquiries described in paragraph (1).\n##### (b) Administration of NICS checks\nNot later than 180 days after the date of enactment of this Act, the Inspector General of the Department of Justice shall submit a report to Congress regarding the percentage of NICS inquiries during the period of calendar years 2014 through 2024 with respect to the transfer of a firearm which were administered by the Federal Bureau of Investigation on behalf of the Bureau of Alcohol, Tobacco, Firearms, and Explosives.\n##### (c) Memorandum of understanding\nNot later than 180 days after the date of enactment of this Act, the Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives and the Director of the Federal Bureau of Investigation shall enter into a memorandum of understanding regarding the administration and processing of NICS inquiries with respect to the transfer of firearms.\n##### (d) Definitions\nIn this section\u2014\n**(1) Firearm**\nThe term firearm has the same meaning given such term under section 5845(a) of the Internal Revenue Code of 1986.\n**(2) NICS**\nThe term NICS means the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ).",
      "versionDate": "2025-03-06",
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
        "actionDate": "2025-01-22",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "613",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ATF Transparency Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-28T12:30:58Z"
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
          "measure-id": "id119s884",
          "measure-number": "884",
          "measure-type": "s",
          "orig-publish-date": "2025-03-06",
          "originChamber": "SENATE",
          "update-date": "2025-09-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s884v00",
            "update-date": "2025-09-05"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>ATF Transparency Act</strong></p><p>This bill modifies procedural requirements related to the transfer or making of firearms that are subject to regulation under the National Firearms Act (e.g., machine guns, short-barreled shotguns, and silencers).</p><p>The bill generally permits the transfer of a firearm if three business\u00a0days have elapsed since the application to transfer the firearm was filed, and the application has not been denied. Additionally, the bill establishes an administrative relief process with respect to an application to transfer that is denied.</p><p>The bill permits the making of a firearm if three business\u00a0days have elapsed since the application to make the firearm was filed,\u00a0and the application has not been denied.</p><p>Finally, the bill requires reports on firearms-related background check inquiries that remain unresolved after 90 days and the percentage of firearms-related background check inquiries related to the transfer of a firearm that were administered by the Federal Bureau of Investigation.</p>"
        },
        "title": "ATF Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s884.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>ATF Transparency Act</strong></p><p>This bill modifies procedural requirements related to the transfer or making of firearms that are subject to regulation under the National Firearms Act (e.g., machine guns, short-barreled shotguns, and silencers).</p><p>The bill generally permits the transfer of a firearm if three business\u00a0days have elapsed since the application to transfer the firearm was filed, and the application has not been denied. Additionally, the bill establishes an administrative relief process with respect to an application to transfer that is denied.</p><p>The bill permits the making of a firearm if three business\u00a0days have elapsed since the application to make the firearm was filed,\u00a0and the application has not been denied.</p><p>Finally, the bill requires reports on firearms-related background check inquiries that remain unresolved after 90 days and the percentage of firearms-related background check inquiries related to the transfer of a firearm that were administered by the Federal Bureau of Investigation.</p>",
      "updateDate": "2025-09-05",
      "versionCode": "id119s884"
    },
    "title": "ATF Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>ATF Transparency Act</strong></p><p>This bill modifies procedural requirements related to the transfer or making of firearms that are subject to regulation under the National Firearms Act (e.g., machine guns, short-barreled shotguns, and silencers).</p><p>The bill generally permits the transfer of a firearm if three business\u00a0days have elapsed since the application to transfer the firearm was filed, and the application has not been denied. Additionally, the bill establishes an administrative relief process with respect to an application to transfer that is denied.</p><p>The bill permits the making of a firearm if three business\u00a0days have elapsed since the application to make the firearm was filed,\u00a0and the application has not been denied.</p><p>Finally, the bill requires reports on firearms-related background check inquiries that remain unresolved after 90 days and the percentage of firearms-related background check inquiries related to the transfer of a firearm that were administered by the Federal Bureau of Investigation.</p>",
      "updateDate": "2025-09-05",
      "versionCode": "id119s884"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s884is.xml"
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
      "title": "ATF Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ATF Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to require the Bureau of Alcohol, Tobacco, Firearms, and Explosives to establish an administrative relief process for individuals whose applications for transfer and registration of a firearm were denied, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:32Z"
    }
  ]
}
```
