# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/817?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/817
- Title: Falun Gong Protection Act
- Congress: 119
- Bill type: S
- Bill number: 817
- Origin chamber: Senate
- Introduced date: 2025-03-03
- Update date: 2026-03-30T22:42:00Z
- Update date including text: 2026-03-30T22:42:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in Senate
- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-03-03: Introduced in Senate

## Actions

- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/817",
    "number": "817",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Falun Gong Protection Act",
    "type": "S",
    "updateDate": "2026-03-30T22:42:00Z",
    "updateDateIncludingText": "2026-03-30T22:42:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T21:14:59Z",
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
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "WI"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NC"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "SD"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "IN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s817is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 817\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Mr. Cruz (for himself, Mr. Johnson , Mr. Scott of Florida , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo provide for the imposition of sanctions with respect to forced organ harvesting within the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Falun Gong Protection Act .\n#### 2. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto avoid any cooperation with the People's Republic of China in the organ transplantation field while the Chinese Communist Party remains in power;\n**(2)**\nto take appropriate measures, including using relevant sanctions authorities, to coerce the Chinese Communist Party to end any state-sponsored organ harvesting campaign;\n**(3)**\nto work with allies, partners, and multilateral institutions to highlight the People's Republic of China\u2019s persecution of Falun Gong; and\n**(4)**\nto coordinate closely with the international community on targeted sanctions and visa restrictions.\n#### 3. Imposition of sanctions with respect to forced organ harvesting within the People\u2019s Republic of China\n##### (a) Imposition of sanctions\nThe President shall impose the sanctions described in subsection (c) with respect to each foreign person included in the most recent list submitted under subsection (b).\n##### (b) List of persons\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the President shall submit to the appropriate congressional committees a list of foreign persons that the President determines to have knowingly and directly engaged in or facilitated the involuntary harvesting of organs within the People\u2019s Republic of China.\n**(2) Updates of lists**\nThe President shall submit to the appropriate congressional committees an updated list under paragraph (1)\u2014\n**(A)**\nas new information becomes available;\n**(B)**\nnot later than one year after the date of the enactment of this Act; and\n**(C)**\nannually thereafter until the date of termination under subsection (h).\n**(3) Form**\nThe list required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n##### (c) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Blocking of property**\nThe President shall exercise all of the powers granted to the President by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) (except that the requirements of section 202 of such Act ( 50 U.S.C. 1701 ) shall not apply) to the extent necessary to block and prohibit all transactions in property and interests in property of a foreign person on the most recent list submitted under subsection (b) if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Inadmissibility of certain individuals**\n**(A) Ineligibility for visas, admission, or parole**\nAn alien included in the most recent list submitted under subsection (b) is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visa revoked**\n**(i) In general**\nAn alien described in subparagraph (A) is subject to revocation of any visa or other entry documentation regardless of when the visa or other entry documentation is or was issued.\n**(ii) Immediate effect**\nA revocation under clause (i) shall\u2014\n**(I)**\ntake effect immediately; and\n**(II)**\nautomatically cancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n**(3) Exception**\nSanctions under paragraph (2) shall not apply to an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations of the United States.\n##### (d) Penalties\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to a person who violates, attempts to violate, conspires to violate, or causes a violation of regulations promulgated to carry out subsection (a) to the same extent that such penalties apply to a person who commits an unlawful act described in section 206(a) of that Act.\n##### (e) Exception To comply with national security\nThe following activities shall be exempt from sanctions under this section:\n**(1)**\nActivities subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ).\n**(2)**\nAny authorized intelligence or law enforcement activities of the United States.\n##### (f) Exception relating to provision of humanitarian assistance\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(1)**\nthe sale of agricultural commodities, food, or medicine;\n**(2)**\nthe provision of vital humanitarian assistance;\n**(3)**\nfinancial transactions relating to humanitarian assistance or for humanitarian purposes; or\n**(4)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance or humanitarian purposes.\n##### (g) Waiver authority\n**(1) Waiver**\nThe President may, on a case by case basis, waive the imposition of any sanction under this section if the President determines such waiver is in the vital national security interest of the United States.\n**(2) Reports**\nNot later than 120 days after the date on which the President submits the first list under subsection (b)(1), and every 120 days thereafter until the date of termination under subsection (h), the President shall submit to the appropriate congressional committees a report on the extent to which the President has used the waiver authority under paragraph (1) during the 120-day period preceding submission of the report.\n##### (h) Sunset\nThe authority to impose sanctions under this section shall terminate on the date that is 5 years after the date of the enactment of this Act.\n##### (i) Definitions\nIn this section:\n**(1) Admission; admitted; alien; lawfully admitted for permanent residence**\nThe terms admission , admitted , alien , and lawfully admitted for permanent residence have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(3) Knowingly**\nThe term knowingly , with respect to conduct, a circumstance, or a result, means that a person had actual knowledge, or should have known, of the conduct, the circumstance, or the result.\n**(4) United states person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(C)**\nany person located in the United States.\n#### 4. Report on organ transplant policies and practices of the People\u2019s Republic of China\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of State, in consultation with the Secretary of Health and Human Services and the Director of the National Institutes of Health, shall submit to the appropriate congressional committees a report on the organ transplant policies and practices of the People\u2019s Republic of China.\n##### (b) Matters To be included\nThe report required under subsection (a) shall include\u2014\n**(1)**\na summary of de jure and de facto policies toward organ transplantation in the People's Republic of China, including with respect to prisoners of conscience (including Falun Gong) and other prisoners;\n**(2)**\n**(A)**\nthe number of organ transplants that are known to occur or are estimated to occur on an annual basis in the People's Republic of China;\n**(B)**\nthe number of known or estimated voluntary organ donors in the People's Republic of China;\n**(C)**\nan assessment of the sources of organs for transplant in the People's Republic of China; and\n**(D)**\nan assessment of the time, in days, that it takes to procure an organ for transplant within the Chinese medical system and an assessment of whether such timetable is possible based on the number of known or estimated organ donors in the People's Republic of China;\n**(3)**\na list of all United States grants during the 10 years before the date of the enactment of this Act that have supported research on organ transplantation in the People's Republic of China or in collaboration between a Chinese entity and a United States entity; and\n**(4)**\na determination as to whether the persecution of Falun Gong practitioners within the People\u2019s Republic of China constitutes an atrocity (as such term is defined in section 6 of the Elie Wiesel Genocide and Atrocities Prevention Act of 2018 ( Public Law 115\u2013441 ; 22 U.S.C. 2656 note)).\n##### (c) Form\nThe report required under subsection (a) shall be submitted in unclassified form, but may include a classified annex.\n#### 5. Exception relating to importation of goods\n##### (a) In general\nThe authorities and requirements to impose sanctions authorized under this Act shall not include the authority or requirement to impose sanctions on the importation of goods.\n##### (b) Good defined\nIn this section, the term good means any article, natural or man-made substance, material, supply or manufactured product, including inspection and test equipment, and excluding technical data.\n#### 6. Appropriate congressional committees defined\nIn this Act, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate.",
      "versionDate": "2025-03-03",
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
        "actionDate": "2026-03-05",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "4009",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Falun Gong and Victims of Forced Organ Harvesting Protection Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-06",
        "text": "Received in the Senate and Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "1540",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Falun Gong Protection Act",
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
            "name": "Asia",
            "updateDate": "2025-05-07T13:51:37Z"
          },
          {
            "name": "China",
            "updateDate": "2025-05-07T13:51:37Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-05-07T13:51:37Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-07T13:51:37Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2025-05-07T13:51:37Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-05-07T13:51:38Z"
          },
          {
            "name": "Medical ethics",
            "updateDate": "2025-05-07T13:51:37Z"
          },
          {
            "name": "Organ and tissue donation and transplantation",
            "updateDate": "2025-05-07T13:51:37Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-05-07T13:51:37Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-05-07T13:51:38Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-05-07T13:51:37Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2025-05-07T13:51:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-16T15:03:42Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s817is.xml"
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
      "title": "Falun Gong Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Falun Gong Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T01:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the imposition of sanctions with respect to forced organ harvesting within the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T01:48:27Z"
    }
  ]
}
```
