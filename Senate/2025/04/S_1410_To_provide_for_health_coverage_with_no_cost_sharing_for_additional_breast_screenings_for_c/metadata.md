# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1410?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1410
- Title: Find It Early Act
- Congress: 119
- Bill type: S
- Bill number: 1410
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-13T17:32:17Z
- Update date including text: 2026-04-13T17:32:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1410",
    "number": "1410",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Find It Early Act",
    "type": "S",
    "updateDate": "2026-04-13T17:32:17Z",
    "updateDateIncludingText": "2026-04-13T17:32:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
            "date": "2025-04-10T15:42:29Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-10T15:42:29Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "KS"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "MS"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "CA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "ME"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "MD"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "WA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1410is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1410\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Ms. Klobuchar (for herself and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide for health coverage with no cost-sharing for additional breast screenings for certain individuals at greater risk for breast cancer.\n#### 1. Short title\nThis Act may be cited as the Find It Early Act .\n#### 2. Coverage with no cost-sharing for additional breast screenings for certain individuals at greater risk for breast cancer\n##### (a) Coverage under group health plans and group and individual health insurance coverage\n**(1) In general**\nSection 2713(a) of the Public Health Service Act ( 42 U.S.C. 300gg\u201313(a) ) is amended\u2014\n**(A)**\nin paragraph (2), by striking and at the end;\n**(B)**\nin paragraph (3), by striking the period at the end and inserting a semicolon;\n**(C)**\nin paragraph (4), by striking the period at the end and inserting and as described in subparagraph (E); and ;\n**(D)**\nby redesignating paragraphs (1) through (5) as subparagraphs (A) through (E), respectively, and adjusting the margins accordingly;\n**(E)**\nby striking the subsection designation and heading and all that follows through A group health plan and inserting the following:\n(a) Requirements (1) In general A group health plan ;\n**(F)**\nin the undesignated matter following subparagraph (E) of paragraph (1) (as so redesignated), by striking Nothing in this subsection and inserting the following:\n(3) Rule of construction Nothing in this subsection ;\n**(G)**\nin subparagraph (E) of paragraph (1) (as so redesignated), by striking (E) for the purposes of this Act, and inserting the following:\n(2) Recommendations For the purposes of this Act, ;\n**(H)**\nin paragraph (1) (as so redesignated), by adding at the end the following:\n(E) (i) with respect to an individual who is at increased risk of breast cancer (as determined in accordance with the most recent applicable American College of Radiology Appropriateness Criteria or the most recent applicable guidelines of the National Comprehensive Cancer Network) or with heterogeneously or extremely dense breast tissue (as defined by the Breast Imaging Reporting and Data System established by the American College of Radiology), screening and diagnostic imaging (with no limitation applied on frequency) for the detection of breast cancer, including 2D or 3D mammograms, breast ultrasounds, breast magnetic resonance imaging, molecular breast imaging, or other technologies (as determined in accordance with such applicable criteria or guidelines); and (ii) with respect to an individual who is not described in subparagraph (A) and who is determined by a health care provider (in accordance with such most recent applicable criteria or guidelines) to require screening or diagnostic breast imaging by reason of factors, including age, race, ethnicity, or personal or family medical history, screening and diagnostic imaging (with no limitation applied on frequency) for the detection of breast cancer, including 2D or 3D mammograms, breast ultrasounds, breast magnetic resonance imaging, molecular breast imaging, or other technologies (as determined in accordance with such applicable criteria or guidelines). .\n**(2) Effective date**\nThe amendments made by paragraph (1) shall apply with respect to plan years beginning on or after January 1, 2026.\n**(3) Application to grandfathered health plans**\nSection 1251(a)(4)(A) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18011(a)(4)(A) ) is amended\u2014\n**(A)**\nby striking title) and inserting title, or as added after the date of the enactment of this Act) ;\n**(B)**\nby redesignating clause (iv) as clause (v); and\n**(C)**\nby inserting after clause (iii) the following:\n(iv) Section 2713(a)(1)(E) (relating to screening and diagnostic imaging for the detection of breast cancer). .\n##### (b) Coverage under Medicare\n**(1) In general**\nSection 1861(ddd)(1)(B) of the Social Security Act ( 42 U.S.C. 1395x(ddd)(1)(B) ) is amended\u2014\n**(A)**\nby striking (B) recommended and inserting (B)(i) recommended ;\n**(B)**\nby striking Task Force; and and inserting Task Force; or ; and\n**(C)**\nby adding at the end the following new clause:\n(ii) beginning on January 1, 2026, in addition to any other items or services described in this paragraph, screening and diagnostic imaging (with no limitation applied on frequency) for the detection of breast cancer, including 2D or 3D mammograms, breast ultrasounds, breast magnetic resonance imaging, molecular breast imaging, or other technologies (as determined in accordance with the most recent applicable American College of Radiology Appropriateness Criteria or the most recent applicable guidelines of the National Comprehensive Cancer Network) for\u2014 (I) an individual who is at increased risk of breast cancer (as determined in accordance with such applicable criteria or guidelines) or with heterogeneously or extremely dense breast tissue (as defined by the Breast Imaging Reporting and Data System established by the American College of Radiology); and (II) an individual who is not described in subclause (I) and who is determined by a health care provider (in accordance with such most recent applicable criteria or guidelines) to require such screening or diagnostic breast imaging by reason of factors determined by the Secretary, including age, race, ethnicity, or personal or family medical history; and .\n**(2) Application of no cost-sharing under Medicare advantage plans**\nSection 1852(a)(1)(B) of the Social Security Act ( 42 U.S.C. 1395w\u201322(a)(1)(B) ) is amended\u2014\n**(A)**\nin clause (iv)\u2014\n**(i)**\nby redesignating subclause (VIII) as subclause (IX); and\n**(ii)**\nby inserting after subclause (VII) the following:\n(VIII) Beginning on January 1, 2026, screening and diagnostic imaging and other technologies described in section 1861(ddd)(1)(B)(ii) furnished to an individual described in such section. ; and\n**(B)**\nin clause (v), by striking and (VI) and inserting (VI), and (VIII) .\n##### (c) Coverage under Medicaid\n**(1) In general**\nSection 1905(a) of the Social Security Act ( 42 U.S.C. 1396d(a) ) is amended\u2014\n**(A)**\nin paragraph (4)\u2014\n**(i)**\nby striking ; and (D) and inserting ; (D) ;\n**(ii)**\nby striking ; and (E) and inserting ; (E) ;\n**(iii)**\nby striking ; and (F) and inserting ; (F) ; and\n**(iv)**\nby inserting before the semicolon at the end the following: ; and (G)(i) with respect to an individual who is at increased risk of breast cancer (as determined in accordance with the most recent applicable American College of Radiology Appropriateness Criteria or the most recent applicable guidelines of the National Comprehensive Cancer Network) or with heterogeneously or extremely dense breast tissue (as defined by the Breast Imaging Reporting and Data System established by the American College of Radiology), in addition to any other item or service described in this subsection, screening and diagnostic imaging (with no limitation applied on frequency) for the detection of breast cancer, including 2D or 3D mammograms, breast ultrasounds, breast magnetic resonance imaging, molecular breast imaging, or other technologies (as determined in accordance with such applicable criteria or guidelines); and (ii) with respect to an individual who is not described in clause (i) and who is determined by a health care provider (in accordance with such most recent applicable criteria or guidelines) to require screening or diagnostic breast imaging by reason of factors, including age, race, ethnicity, or personal or family medical history, screening and diagnostic imaging (with no limitation applied on frequency) for the detection of breast cancer, including 2D or 3D mammograms, breast ultrasounds, breast magnetic resonance imaging, molecular breast imaging, or other technologies (as determined in accordance with such applicable criteria or guidelines) ; and\n**(B)**\nin paragraph (13), in the matter preceding subparagraph (A), by inserting (other than an item or service for which medical assistance is provided pursuant to paragraph (4)(G)) after services .\n**(2) No cost-sharing for certain breast cancer screening and diagnostic imaging**\n**(A) In general**\nSubsections (a)(2) and (b)(2) of section 1916 of the Social Security Act ( 42 U.S.C. 1396o ) are each amended\u2014\n**(i)**\nin subparagraph (I), by striking or at the end;\n**(ii)**\nin subparagraph (J), by striking at the end ; and and inserting , or ; and\n**(iii)**\nby adding at the end the following subparagraph:\n(K) with respect to an individual described in clause (i) or (ii) of section 1905(a)(4)(G), screening and diagnostic imaging and other technologies described in such clause (i) or (ii), respectively; and .\n**(B) Application to alternative cost-sharing**\nSection 1916A(b)(3)(B) of the Social Security Act ( 42 U.S.C. 1396o\u20131(b)(3)(B) ) is amended by adding at the end the following new clause:\n(xv) With respect to an individual described in clause (i) or (ii) of section 1905(a)(4)(G), screening and diagnostic imaging and other technologies described in such clause (i) or (ii), respectively. .\n**(3) Inclusion in benchmark coverage**\nSection 1937(b) of the Social Security Act ( 42 U.S.C. 1396u\u20137(b) ) is amended by adding at the end the following new paragraph:\n(9) Coverage of certain breast cancer screening and diagnostic imaging for certain individuals Notwithstanding the previous provisions of this section, a State may not provide for medical assistance through enrollment of an individual with benchmark coverage or benchmark-equivalent coverage under this section unless such coverage includes medical assistance, with respect to an individual described in clause (i) or (ii) of section 1905(a)(4)(G), for screening and diagnostic imaging and other technologies described in such clause (i) or (ii), respectively. .\n**(4) Effective date**\n**(A) In general**\nExcept as provided in subparagraph (B), the amendments made by this subsection shall take effect on January 1, 2026.\n**(B) Delay permitted if State legislation required**\nIn the case of a State plan approved under title XIX of the Social Security Act which the Secretary of Health and Human Services determines requires State legislation (other than legislation appropriating funds) in order for the plan to meet the additional requirements imposed by this section, the State plan shall not be regarded as failing to comply with the requirements of such title solely on the basis of the failure of the plan to meet such additional requirements before the first day of the first calendar quarter beginning after the close of the first regular session of the State legislature that ends after the 1-year period beginning with the date of the enactment of this section. For purposes of the preceding sentence, in the case of a State that has a 2-year legislative session, each year of the session is deemed to be a separate regular session of the State legislature.\n##### (d) Coverage and elimination of cost-Sharing under TRICARE\n**(1) Coverage**\nTitle 10, United States Code, is amended\u2014\n**(A)**\nin section 1074d(a), by adding at the end the following new paragraph:\n(3) Any member or former member of the uniformed services who is entitled to medical care under section 1074 or 1074a of this title and is an individual described in subparagraph (B) of section 1079(a)(20) of this title shall also be entitled to the items and services described in subparagraph (A) of such section (subject to the same limitations specified in such subparagraph), as part of such medical care. ; and\n**(B)**\nin section 1079(a), by adding at the end the following new paragraph:\n(20) (A) Screening and diagnostic imaging (with no limitation applied on frequency) for the detection of breast cancer, including 2D or 3D mammograms, breast ultrasounds, breast magnetic resonance imaging, molecular breast imaging, or other technologies (as determined in accordance with the most recent applicable criteria or guidelines described in subparagraph (B)), shall be provided if the patient is an individual described in subparagraph (B). (B) An individual described in this subparagraph is\u2014 (i) an individual who is at increased risk of breast cancer (as determined in accordance with the most recent applicable American College of Radiology Appropriateness Criteria or the most recent applicable guidelines of the National Comprehensive Cancer Network) or with heterogeneously or extremely dense breast tissue (as defined by the Breast Imaging Reporting and Data System established by the American College of Radiology); or (ii) an individual who is not described in clause (i) and who is determined by a health care provider (in accordance with such most recent applicable criteria or guidelines) to require screening or diagnostic breast imaging by reason of factors including age, race, ethnicity, or personal or family medical history. .\n**(2) Elimination of cost-sharing**\nSuch title is further amended\u2014\n**(A)**\nin section 1075a, by adding at the end the following new subsection:\n(d) Elimination of cost-Sharing for certain breast cancer-Related items and services Notwithstanding any other provision of this section, cost-sharing requirements may not be imposed or collected with respect to any beneficiary enrolled in TRICARE Prime for any item or service described in subparagraph (A) of section 1079(a)(20) of this title provided under TRICARE Prime, in accordance with the limitations specified in such subparagraph, if the beneficiary is an individual described in subparagraph (B) of such section. ;\n**(B)**\nin section 1075(c), by adding at the end the following new paragraph:\n(5) Notwithstanding any other provision of this section, cost-sharing requirements may not be imposed or collected with respect to any beneficiary enrolled in TRICARE Select for any item or service described in subparagraph (A) of section 1079(a)(20) of this title provided under TRICARE Select, in accordance with the limitations specified in such subparagraph, if the beneficiary is an individual described in subparagraph (B) of such section. ; and\n**(C)**\nin section 1086, by adding at the end the following new subsection:\n(j) Notwithstanding any other provision of this section, cost-sharing may not be imposed or collected under a plan contracted for under subsection (a) with respect to any individual described in subparagraph (B) of section 1079(a)(20) of this title for an item or service described in subparagraph (A) of such section and provided in accordance with the limitations specified in such subparagraph. .\n**(3) Effective date**\nThe amendments made by this subsection shall take effect on January 1, 2026.\n##### (e) Coverage and elimination of cost-Sharing with respect to veterans\n**(1) Coverage and elimination of cost-sharing**\nSubchapter II of chapter 17 of title 38, United States Code, is amended by inserting after section 1720J the following new section:\n1720K. Breast screenings for certain individuals at increased risk for breast cancer (a) Coverage of items and services (1) Coverage The Secretary shall furnish to a veteran described in paragraph (2) screening and diagnostic imaging (with no limitation applied on frequency) for the detection of breast cancer, including 2D or 3D mammograms, breast ultrasounds, breast magnetic resonance imaging, molecular breast imaging, or other technologies (as determined in accordance with the most recent applicable criteria or guidelines described in such paragraph) pursuant to this section. (2) Eligibility A veteran described in this paragraph is\u2014 (A) a veteran who is at increased risk of breast cancer (as determined in accordance with the most recent applicable American College of Radiology Appropriateness Criteria or the most recent applicable guidelines of the National Comprehensive Cancer Network) or with heterogeneously or extremely dense breast tissue (as defined by the Breast Imaging Reporting and Data System established by the American College of Radiology), without regard to whether the veteran is enrolled in the system of annual patient enrollment established and operated under section 1705(a) of this title; or (B) a veteran who is not described in subparagraph (A) and who is determined by a health care provider (in accordance with such most recent applicable criteria or guidelines) to require screening or diagnostic breast imaging by reason of factors including age, race, ethnicity, or personal or family medical history, without regard to whether the veteran is enrolled in the system of annual patient enrollment established and operated under section 1705(a) of this title. (b) Prohibition on cost-Sharing Notwithstanding subsections (f) and (g) of section 1710 and section 1722A of this title, the Secretary may not require any veteran described in paragraph (2) of subsection (a) to make any copayment for, or charge the veteran for any other cost of, the receipt of any item or service furnished pursuant to paragraph (1) of such subsection. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1720J the following new item:\n1720K. Breast screenings for certain individuals at increased risk for breast cancer. .\n**(3) Effective date**\nThe amendments made by this subsection shall take effect on January 1, 2026.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2026-01-15",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "6182",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Find It Early Act",
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
        "updateDate": "2025-05-21T10:38:25Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1410is.xml"
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
      "title": "Find It Early Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Find It Early Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for health coverage with no cost-sharing for additional breast screenings for certain individuals at greater risk for breast cancer.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:48:17Z"
    }
  ]
}
```
