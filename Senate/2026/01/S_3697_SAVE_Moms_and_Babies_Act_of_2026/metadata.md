# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3697?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3697
- Title: SAVE Moms and Babies Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3697
- Origin chamber: Senate
- Introduced date: 2026-01-27
- Update date: 2026-05-14T11:03:27Z
- Update date including text: 2026-05-14T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in Senate
- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S292)
- Latest action: 2026-01-27: Introduced in Senate

## Actions

- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S292)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3697",
    "number": "3697",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "SAVE Moms and Babies Act of 2026",
    "type": "S",
    "updateDate": "2026-05-14T11:03:27Z",
    "updateDateIncludingText": "2026-05-14T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S292)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T21:49:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sponsorshipDate": "2026-01-27",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "ID"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "SD"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "MS"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "OK"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "KY"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "WY"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "TX"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "IN"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "KS"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "AL"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "FL"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "MO"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "ID"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NC"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "SC"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "LA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "TX"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "IA"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "UT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "ND"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NE"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NE"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "LA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "ND"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "IN"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "TN"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "AR"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "KS"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "TN"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "WY"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AL"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3697is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3697\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Mrs. Hyde-Smith (for herself, Mr. Daines , Mr. Risch , Mr. Rounds , Mr. Wicker , Mr. Lankford , Mr. McConnell , Ms. Lummis , Mr. Cruz , Mr. Banks , Mr. Marshall , Mrs. Britt , Mr. Scott of Florida , Mr. Hawley , Mr. Crapo , Mr. Budd , Mr. Graham , Mr. Cassidy , Mr. Cornyn , Ms. Ernst , Mr. Lee , Mr. Cramer , Mr. Ricketts , Mrs. Fischer , Mr. Kennedy , Mr. Hoeven , Mr. Young , Mr. Hagerty , Mr. Cotton , Mr. Moran , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to prohibit the approval of new abortion drugs, to prohibit investigational use exemptions for abortion drugs, and to impose additional regulatory requirements with respect to previously approved abortion drugs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Support And Value Expectant Moms and Babies Act of 2026 or the SAVE Moms and Babies Act of 2026 .\n#### 2. Abortion drugs prohibited\n##### (a) In general\nSection 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) is amended\u2014\n**(1)**\nby redesignating the second subsection (z), as added by section 3601(a) of division FF of Public Law 117\u2013328 , as subsection (aa); and\n**(2)**\nby adding at the end the following:\n(bb) Abortion drugs (1) Prohibitions The Secretary shall not approve\u2014 (A) any application submitted under subsection (b) or (j) for marketing an abortion drug; or (B) grant an investigational use exemption under subsection (i) for\u2014 (i) an abortion drug; or (ii) any investigation in which the unborn child of a woman known to be pregnant is knowingly destroyed. (2) Previously approved abortion drugs If an approval described in paragraph (1) is in effect for an abortion drug as of the date of enactment of the Support And Value Expectant Moms and Babies Act of 2026 , the Secretary shall\u2014 (A) not approve any labeling change\u2014 (i) to approve the use of such abortion drug after 70 days gestation; or (ii) to approve the dispensing of such abortion drug by any means other than in-person administration by the prescribing health care practitioner; (B) treat such abortion drug as subject to section 503(b)(1); and (C) require such abortion drug to be subject to a risk evaluation and mitigation strategy under section 505\u20131 that at a minimum\u2014 (i) requires health care practitioners who prescribe such abortion drug\u2014 (I) to be certified in accordance with the strategy; and (II) to not be acting in their capacity as a pharmacist; (ii) as part of the certification process referred to in clause (i), requires such practitioners\u2014 (I) to have the ability to assess the duration of pregnancy accurately; (II) to have the ability to diagnose ectopic pregnancies; (III) to have the ability to provide surgical intervention in cases of incomplete abortion or severe bleeding; (IV) to have the ability to ensure patient access to medical facilities equipped to provide blood transfusions and resuscitation, if necessary; and (V) to report any deaths or other adverse events associated with the use of such abortion drug to the Food and Drug Administration and to the manufacturer of such abortion drug, identifying the patient by a non-identifiable reference and the serial number from each package of such abortion drug; (iii) limits the dispensing of such abortion drug to patients\u2014 (I) in a clinic, medical office, or hospital by means of in-person administration by the prescribing health care practitioner; and (II) not in pharmacies or any setting other than the health care settings described in subclause (I); (iv) requires the prescribing health care practitioner to give to the patient documentation on any risk of serious complications associated with use of such abortion drug and receive acknowledgment of such receipt from the patient; (v) requires all known adverse events associated with such abortion drug to be reported, excluding any individually identifiable patient information, to the Food and Drug Administration by the\u2014 (I) manufacturers of such abortion drug; and (II) prescribers of such abortion drug; and (vi) requires reporting of administration of the abortion drug as required by State law, or in the absence of a State law regarding such reporting, in the same manner as a surgical abortion. (3) Reporting on adverse events by other health care practitioners The Secretary shall require all other health care practitioners to report to the Food and Drug Administration any adverse events experienced by their patients that are connected to use of an abortion drug, excluding any individually identifiable patient information. (4) Rule of construction Nothing in this section shall be construed to restrict the authority of the Federal Government, or of a State, to establish, implement, and enforce requirements and restrictions with respect to abortion drugs under provisions of law other than this section that are in addition to the requirements and restrictions under this section. (5) Definitions In this section: (A) The term abortion drug means any drug, substance, or combination of drugs or substances that is intended for use or that is in fact used (irrespective of how the product is labeled) to intentionally kill the unborn child of a woman known to be pregnant, or to intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) to produce a live birth; (ii) to remove a dead unborn child; or (iii) to treat an ectopic pregnancy. (B) The term adverse event includes each of the following: (i) A fatality. (ii) An ectopic pregnancy. (iii) A hospitalization. (iv) A blood loss requiring a transfusion. (v) An infection, including endometritis, pelvic inflammatory disease, and pelvic infections with sepsis. (vi) A severe infection. (C) The term gestation means the period of days of pregnancy beginning on the first day of the last menstrual period. (D) The term health care practitioner means any individual who is licensed, registered, or otherwise permitted, by the United States or the jurisdiction in which the individual practices, to prescribe drugs subject to section 503(b)(1). (E) The term unborn child means an individual organism of the species homo sapiens, beginning at fertilization, until the point of being born alive as defined in section 8(b) of title 1, United States Code. .\n##### (b) Ongoing investigational use\nIn the case of any investigational use of a drug pursuant to an investigational use exemption under section 505(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(i) ) that was granted before the date of enactment of this Act, such exemption is deemed to be rescinded as of the day that is 3 years after the date of enactment of this Act if the Secretary would be prohibited by section 505(bb)(1)(B) of the Federal Food, Drug, and Cosmetic Act, as added by subsection (a), from granting such exemption as of such day.",
      "versionDate": "2026-01-27",
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
        "actionDate": "2025-01-23",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "685",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAVE Moms and Babies Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-02-20T13:45:54Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3697is.xml"
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
      "title": "SAVE Moms and Babies Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAVE Moms and Babies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Support And Value Expectant Moms and Babies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act to prohibit the approval of new abortion drugs, to prohibit investigational use exemptions for abortion drugs, and to impose additional regulatory requirements with respect to previously approved abortion drugs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:31Z"
    }
  ]
}
```
