# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3917?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3917
- Title: The Dalilah Law
- Congress: 119
- Bill type: S
- Bill number: 3917
- Origin chamber: Senate
- Introduced date: 2026-02-25
- Update date: 2026-05-01T11:03:33Z
- Update date including text: 2026-05-01T11:03:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in Senate
- 2026-02-25 - IntroReferral: Introduced in Senate
- 2026-02-25 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-25: Introduced in Senate

## Actions

- 2026-02-25 - IntroReferral: Introduced in Senate
- 2026-02-25 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3917",
    "number": "3917",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
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
    "title": "The Dalilah Law",
    "type": "S",
    "updateDate": "2026-05-01T11:03:33Z",
    "updateDateIncludingText": "2026-05-01T11:03:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T20:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "ID"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "OK"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "WV"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "MO"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "WV"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "MS"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3917is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3917\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2026 Mr. Banks (for himself, Mr. Risch , Mr. Lankford , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit the issuance of commercial driver\u2019s licenses to individuals who are not citizens or lawful permanent residents of the United States or holders of certain work visas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as The Dalilah Law .\n#### 2. Prohibition on issuance of CDLs to individuals who are not citizens or lawful permanent residents of the United States or holders of certain work visas\n##### (a) Definitions\nIn this section:\n**(1) Commercial driver\u2019s license**\nThe term commercial driver\u2019s license has the meaning given the term in section 31301 of title 49, United States Code.\n**(2) Commercial motor vehicle**\nThe term commercial motor vehicle has the meaning given the term in section 31301 of title 49, United States Code.\n**(3) Covered examination**\nThe term covered examination means any test or examination relating to the issuance or renewal of a covered license or authorization, including\u2014\n**(A)**\na commercial driver\u2019s license knowledge test;\n**(B)**\na commercial driver\u2019s license skills test; and\n**(C)**\nany other test or examination required to acquire, maintain, or upgrade a covered license or authorization.\n**(4) Covered funding**\nThe term covered funding , with respect to a State, means any funding that is authorized to be provided by the Secretary to that State, or for a project or activity carried out in that State, under any provision of Federal law (including regulations).\n**(5) Covered license or authorization**\nThe term covered license or authorization means\u2014\n**(A)**\na commercial driver\u2019s license, including a non-domiciled commercial driver\u2019s license; and\n**(B)**\nany other license or authorization issued by a State authorizing an individual to operate a commercial motor vehicle.\n**(6) Non-domiciled commercial driver\u2019s license**\nThe term non-domiciled commercial driver\u2019s license means a commercial driver\u2019s license issued by a State or other jurisdiction to an individual who is not domiciled in that State or jurisdiction, in accordance with part 383 of title 49, Code of Federal Regulations (or successor regulations).\n##### (b) Prohibition\nSection 31311(a)(12) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby striking who operates and inserting the following: \u201cwho\u2014\n(i) operates ;\n**(B)**\nin clause (i) (as so designated), by striking vehicle and is and inserting the following: \u201cvehicle;\n(ii) is ; and\n**(C)**\nin clause (ii) (as so designated), by striking State. and inserting the following: \u201cState; and\n(iii) is a citizen or lawful permanent resident of the United States. ;\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nin clause (i), by striking and at the end;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iii) (I) is a citizen or lawful permanent resident of the United States; or (II) is a nonimmigrant described in subparagraph (E)(ii), (H)(ii)(a), or (H)(ii)(b) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) and is in possession of a valid, unexpired nonimmigrant visa issued to the individual pursuant to any such subparagraph. ; and\n**(3)**\nin subparagraph (C)\u2014\n**(A)**\nin clause (ii)(II), by striking and at the end;\n**(B)**\nin clause (iii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iv) (I) is a citizen or lawful permanent resident of the United States; or (II) is a nonimmigrant described in subparagraph (E)(ii), (H)(ii)(a), or (H)(ii)(b) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) and is in possession of a valid, unexpired nonimmigrant visa issued to the individual pursuant to any such subparagraph. .\n##### (c) Disqualifications\nSection 31310 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (d)(2)\u2014\n**(A)**\nby striking paragraph (9) of ; and\n**(B)**\nby striking 7102(9) and inserting 7102 ; and\n**(2)**\nby adding at the end the following:\n(l) Disqualification based on lack of citizenship, lawful permanent residence, or work visa status The Secretary shall disqualify from operating a commercial motor vehicle for life an individual who operates a commercial motor vehicle in the United States while that individual is not a citizen or lawful permanent resident of the United States or a nonimmigrant described in subparagraph (E)(ii), (H)(ii)(a), or (H)(ii)(b) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) in possession of a valid, unexpired nonimmigrant visa issued to the individual pursuant to any such subparagraph, unless such individual\u2014 (1) is operating a commercial motor vehicle as a nonimmigrant described in subparagraph (B) of that section and is in possession of a valid, unexpired nonimmigrant visa issued to the individual pursuant to that subparagraph; or (2) holds a valid travel authorization pursuant to section 217.5 of title 8, Code of Federal Regulations (or any successor regulation), and possesses a valid, unexpired admission record pursuant to section 1302 of title 8, United States Code. .\n##### (d) Recertification\nTo avoid the withholding of covered funding under paragraphs (1) and (2) of subsection (e), a State shall\u2014\n**(1)**\nrequire all individuals who, as of the date of enactment of this Act, hold a covered license or authorization issued by the State to be recertified for that covered license or authorization not later than 180 days after the date of enactment of this Act, which recertification shall include verification that the individual\u2014\n**(A)**\nis\u2014\n**(i)**\na citizen or lawful permanent resident of the United States; or\n**(ii)**\na nonimmigrant described in subparagraph (E)(ii), (H)(ii)(a), or (H)(ii)(b) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) in possession of a valid, unexpired nonimmigrant visa issued to the individual pursuant to any such subparagraph;\n**(B)**\nis proficient in the English language, as described in section 391.11(b)(2) of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act); and\n**(C)**\nhas passed all covered examinations relating to the covered license or authorization in English; and\n**(2)**\nrevoke the covered license or authorization of any individual who\u2014\n**(A)**\nfails to recertify by the deadline described in paragraph (1); or\n**(B)**\non recertification under that paragraph, is found\u2014\n**(i)**\nto be neither\u2014\n**(I)**\na citizen or lawful permanent resident of the United States; or\n**(II)**\na nonimmigrant described in subparagraph (E)(ii), (H)(ii)(a), or (H)(ii)(b) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) in possession of a valid, unexpired nonimmigrant visa issued to the individual pursuant to any such subparagraph;\n**(ii)**\nnot to be proficient in the English language, as described in section 391.11(b)(2) of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act); or\n**(iii)**\nnot to have passed all covered examinations relating to the covered license or authorization in English.\n##### (e) Withholding of covered funding\n**(1) Withholding for recertification failure**\nNotwithstanding any other provision of law, beginning with the first fiscal year beginning after the deadline for recertifications under subsection (d)(1), the Secretary shall withhold all covered funding from a State that fails to complete those recertifications by that deadline.\n**(2) Withholding for revocation failure**\nNotwithstanding any other provision of law, beginning with the first fiscal year beginning after the deadline for recertifications under subsection (d)(1), the Secretary shall withhold all covered funding from a State that fails to complete the revocations described in subsection (d)(2) by that deadline.\n**(3) Witholding for status verification failure**\nNotwithstanding any other provision of law, beginning with the first fiscal year beginning after the date of enactment of this Act, the Secretary shall withhold all covered funding from a State that, after that date of enactment, issues covered licenses or authorizations to individuals who are neither\u2014\n**(A)**\ncitizens or lawful permanent residents of the United States; or\n**(B)**\nnonimmigrants described in subparagraph (E)(ii), (H)(ii)(a), or (H)(ii)(b) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) in possession of a valid, unexpired nonimmigrant visa issued to such individuals pursuant to any such subparagraph.\n**(4) Witholding for English proficiency verification failure**\nNotwithstanding any other provision of law, beginning with the first fiscal year beginning after the date of enactment of this Act, the Secretary shall withhold all covered funding from a State that, after that date of enactment\u2014\n**(A)**\nissues covered licenses or authorizations to individuals who are not proficient in the English language, as described in section 391.11(b)(2) of title 49, Code of Federal Regulations (or a successor regulation); or\n**(B)**\nadministers any covered examination in any language other than English.",
      "versionDate": "2026-02-25",
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
        "actionDate": "2026-03-03",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "7758",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "The Dalilah Law",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-04",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "7793",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "The Dalilah Law",
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
        "name": "Immigration",
        "updateDate": "2026-03-13T15:35:14Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3917is.xml"
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
      "title": "The Dalilah Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T11:03:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "The Dalilah Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the issuance of commercial driver's licenses to individuals who are not citizens or lawful permanent residents of the United States or holders of certain work visas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:32Z"
    }
  ]
}
```
