# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4379
- Title: Russia’s War on Faith Act
- Congress: 119
- Bill type: S
- Bill number: 4379
- Origin chamber: Senate
- Introduced date: 2026-04-22
- Update date: 2026-05-20T11:03:29Z
- Update date including text: 2026-05-20T11:03:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in Senate
- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-04-22: Introduced in Senate

## Actions

- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4379",
    "number": "4379",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Russia\u2019s War on Faith Act",
    "type": "S",
    "updateDate": "2026-05-20T11:03:29Z",
    "updateDateIncludingText": "2026-05-20T11:03:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
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
      "actionDate": "2026-04-22",
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
          "date": "2026-04-23T00:55:15Z",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "RI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4379is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4379\nIN THE SENATE OF THE UNITED STATES\nApril 22, 2026 Mr. Kennedy (for himself and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Secretary of State and the Secretary of Defense to jointly submit a report on efforts by the Government of the Russian Federation to violate the religious freedoms of the people of Ukraine, to require the President to impose all applicable sanctions with respect to foreign persons determined to have engaged in such efforts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Russia\u2019s War on Faith Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nIn territories of Ukraine temporarily occupied by the Russian Federation, Russian occupation authorities have imposed policies that restrict, suppress, and eliminate freedom of religion and belief, in violation of international law and civilian protections under the law of armed conflict.\n**(2)**\nThe United States Commission on International Religious Freedom has documented that Russian authorities in occupied Ukrainian territories have engaged in severe violations of religious freedom, including the detention, torture, disappearance, and unlawful imprisonment of clergy and believers, as well as the closure and confiscation of houses of worship.\n**(3)**\nAccording to Ukrainian authorities and independent monitoring groups, Russian forces have damaged or destroyed more than 600 churches, synagogues, mosques, and other religious sites since the start of the Russian Federation\u2019s full-scale invasion.\n**(4)**\nThe Russian Federation has killed more than 50 Ukrainian priests, pastors, and other religious leaders during the Russian Federation\u2019s invasion, and many others have been abducted, detained, tortured, or forcibly disappeared in occupied territories.\n**(5)**\nProtestant, Catholic, Muslim, members of the Church of Jesus Christ of Latter-Day Saints, Crimean Tatar, and Orthodox Christian communities not aligned with the Russian Orthodox Church have been subjected to raids, forced re-registration under Russian law, intimidation, and criminal prosecution, with many congregations driven underground or permanently shuttered.\n**(6)**\nReligious buildings in occupied areas have been seized and repurposed for military or administrative use, religious literature has been confiscated, and charitable ministries dismantled, eroding both the spiritual and humanitarian foundations of local communities.\n**(7)**\nThe Russian Orthodox Church, led by Patriarch Kirill of Moscow, has publicly framed the invasion in theological terms, describing the war as a holy war having metaphysical significance and stating in a September 2022 sermon that if a soldier dies in the performance of military duty, this sacrifice washes away all the sins that a person has committed . According to the Committee on International Religious Freedom, Russian de facto authorities often commit religious freedom violations to facilitate the dominance of the Russian Orthodox Church of the Moscow Patriarchate in these territories .\n**(8)**\nThe Russian Federation\u2019s actions demonstrate a systematic campaign of religious persecution in occupied Ukrainian territory, violating the fundamental right to freedom of thought, conscience, religion, and belief as protected under the Universal Declaration of Human Rights and the International Covenant on Civil and Political Rights.\n#### 3. Report on the Russian Federation\u2019s persecution of religious groups in occupied territories of Ukraine; imposition of sanctions\n##### (a) Report required\nNot later than 120 days after the date of the enactment of this Act, and annually thereafter for 3 years, the Secretary of State and Secretary of Defense, in coordination with the Director of National Intelligence, shall jointly submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\na detailed description of the Government of the Russian Federation and its state-affiliated, quasi-state, or occupation-era activities that involve the persecution or suppression of, or discrimination against, or otherwise directly or indirectly involve engaging in or facilitating serious human rights abuse against, Christians, Jews, and Muslims (including Crimean Tatars), and other religious minorities not affiliated with the Russian Orthodox Church, and their respective religious organizations in Russian-occupied territories of Ukraine;\n**(2)**\nan identification of churches, synagogues, mosques, other religious facilities, including Christian, Jewish, Muslim, and other minority religious institutions, that have been destroyed, damaged, seized, repurposed, or otherwise appropriated directly or indirectly by persons operating for or on behalf of the Government of the Russian Federation in occupied territories of Ukraine;\n**(3)**\nan assessment of\u2014\n**(A)**\nthe number of Christians, Jews, Muslims (including Crimean Tatars), and other religious minorities who are not affiliated with the Russian Orthodox Church, who have been subjected to persecution, imprisonment, or forced displacement in occupied territories of Ukraine;\n**(B)**\nrestrictions imposed on Christian, Jewish, Muslim, and other religions not affiliated with the Russian Orthodox Church\u2019s religious practices, worship services, or religious education in occupied territories;\n**(C)**\nefforts to compel Christian organizations to affiliate with Moscow-based religious institutions or to suppress Christian activity not affiliated with Moscow-based religions;\n**(D)**\nefforts by the Government of the Russian Federation, by authorities exercising de facto governmental control in occupied territory, or by entities or individuals otherwise affiliated with the Russian Federation, to compel Christian organizations in Ukraine and in occupied territories\u2014\n**(i)**\nto affiliate with Moscow-based religious institutions; or\n**(ii)**\nto suppress Christian, Jewish, Muslim, or any other denominations not aligned with Russian state interests; and\n**(E)**\nthe overall impact of the Russian Federation\u2019s invasion of Ukraine, and its occupation of Ukrainian territory, on religious freedom in occupied territories of Ukraine, including Crimea and Sevastopol; and\n**(4)**\na list of individuals and entities affiliated with the Government of the Russian Federation, or exercising de facto authority in occupied territory, that\u2014\n**(A)**\nare responsible for persecution or suppression of, or discrimination against, Christians, Jews, or Muslims in Ukraine and in the occupied territories of Ukraine; or\n**(B)**\nhave otherwise engaged in or attempted to engage in any of the conduct described in this subsection.\n##### (b) Certification required\nNot later than 30 days after the submission of each report required by subsection (a), the President shall certify to the appropriate congressional committees whether there may be reasonable grounds to determine that any of the individuals and entities included in the list described in subsection (a)(4) have engaged the any of the conduct described in paragraph (2) or (3) of subsection (a).\n##### (c) Effect of positive certification\nIf the President makes an affirmative certification under subsection (b) with respect to a foreign person, the President shall impose applicable sanctions with respect to that person pursuant to the authorities and procedures set forth in the applicable regulations under\u2014\n**(1)**\npart 583 of title 31, Code of Federal Regulations (relating to sanctions authorized under the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 10101 et seq. ));\n**(2)**\npart 589 of title 31, Code of Federal Regulations (relating to Ukraine-/Russia-related sanctions);\n**(3)**\npart 587 of title 31, Code of Federal Regulations (relating to Russian harmful foreign activities sanctions); or\n**(4)**\nany other regulation under chapter V of title 31, Code of Federal Regulations, providing for the imposition of sanctions (including the blocking of property or interests in property) with respect to the conduct for which such person received an affirmative certification.\n##### (d) Effect of subsequent negative determination\nTo the extent that the President determines, based on a subsequent report required by subsection (a), that an individual or entity previously listed in such a report no longer engages in any of the conduct described in subsection (b) or otherwise no longer meets the requirements with respect to the applicable sanctions imposed with respect to such person under subsection (c), the President may waive or terminate the application of such sanctions with respect to that person.\n##### (e) Form\nThe report required by subsection (a) shall be submitted in an unclassified form, but may include a classified annex.\n##### (f) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Armed Services, the Committee on Banking, Housing, and Urban Affairs, the Committee on Foreign Relations, and the Select Committee on Intelligence of the Senate; and\n**(2)**\nthe Committee on Armed Services, the Committee on Financial Services, the Committee on Foreign Affairs, and the Permanent Select Committee on Intelligence of the House of Representatives.",
      "versionDate": "2026-04-22",
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
        "actionDate": "2026-04-22",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on Financial Services, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8433",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Countering Russia\u2019s War on Faith Act",
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
        "updateDate": "2026-05-04T22:36:20Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4379is.xml"
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
      "title": "Russia\u2019s War on Faith Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Russia\u2019s War on Faith Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-02T03:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of State and the Secretary of Defense to jointly submit a report on efforts by the Government of the Russian Federation to violate the religious freedoms of the people of Ukraine, to require the President to impose all applicable sanctions with respect to foreign persons determined to have engaged in such efforts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-02T03:33:35Z"
    }
  ]
}
```
