# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6782?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6782
- Title: Public Health Air Quality Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6782
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-05-12T08:05:59Z
- Update date including text: 2026-05-12T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6782",
    "number": "6782",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001125",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Carter, Troy A. [D-LA-2]",
        "lastName": "Carter",
        "party": "D",
        "state": "LA"
      }
    ],
    "title": "Public Health Air Quality Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:59Z",
    "updateDateIncludingText": "2026-05-12T08:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-12-17T14:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "DC"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OH"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "WA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MI"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "TN"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IN"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "FL"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "TX"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "MA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6782ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6782\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Carter of Louisiana (for himself, Mr. Tonko , Ms. Norton , Mr. Ruiz , Ms. Barrag\u00e1n , Mr. Krishnamoorthi , Mr. Mullin , Ms. Schakowsky , Mr. Landsman , Ms. McClellan , Ms. Jayapal , Ms. Ocasio-Cortez , Ms. Dexter , Mrs. Dingell , Mr. Cohen , Mr. Carson , Mr. Casten , and Ms. Castor of Florida ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo protect clean air and public health by expanding fenceline and ambient air monitoring and access to air quality information for communities affected by air pollution, to require hazardous air pollutant monitoring at the fenceline of facilities whose emissions are linked to local health threats, to ensure the Environmental Protection Agency promulgates rules that require hazardous air pollutant data measurement and electronic submission at fencelines and stacks of industrial source categories, to expand and strengthen the national ambient air quality monitoring network, to deploy air quality systems in communities affected by air pollution, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Health Air Quality Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Accidental release**\nThe term accidental release has the meaning given the term in section 112(r)(2) of the Clean Air Act ( 42 U.S.C. 7412(r)(2) ).\n**(2) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(3) Air quality system**\nThe term air quality system means an air quality sensor or set of sensors installed together with instruments to measure meteorology and store and transmit data.\n**(4) Area source; hazardous air pollutant; major source; new source; stationary source**\nExcept as otherwise provided, the terms area source , hazardous air pollutant , major source , new source , and stationary source have the meanings given those terms in section 112(a) of the Clean Air Act ( 42 U.S.C. 7412(a) ).\n**(5) Cumulative impact**\nThe term cumulative impact means the totality of exposures to combinations of chemical and nonchemical stressors, and the effects of those exposures on health, well-being, and quality of life outcomes.\n**(6) Cumulative risk**\nThe term cumulative risk means the combined risks to health or the environment from multiple agents or stressors.\n**(7) Emissions measurement system**\nThe term emissions measurement system means a set of monitors, testing equipment, tools, and processes employed at a facility to measure emissions from direct and fugitive points at a source or facility or at the fenceline of the source or facility that employs Environmental Protection Agency-approved or promulgated test methods for all measured pollutants for which a method is available.\n**(8) Federal equivalent method; Federal reference method**\nThe terms Federal equivalent method and Federal reference method have the meanings given those terms in section 53.1 of title 40, Code of Federal Regulations (or to the same or substantially similar terms in successor regulations).\n**(9) Method 325A**\nThe term Method 325A means the most current version of the test method 325A published by the Environmental Protection Agency.\n**(10) Method 325B**\nThe term Method 325B means the most current version of the test method 325B published by the Environmental Protection Agency.\n**(11) METHOD 327**\nThe term Method 327 means the most current version of the test method 327 published by the Environmental Protection Agency.\n**(12) Method TO\u201315A**\nThe term Method TO\u201315A means the most current version of the test method TO\u201315 (including TO\u201315A) published by the Environmental Protection Agency.\n**(13) National Air Toxics Trends Network**\nThe term National Air Toxics Trends Network means the long-term hazardous air pollutants monitoring data network established by the Environmental Protection Agency to assess trends and emissions reduction program effectiveness.\n**(14) National ambient air quality standard**\nThe term national ambient air quality standard means a national ambient air quality standard established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ).\n**(15) NCore**\nThe term NCore has the meaning given the term in section 58.1 of title 40, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(16) Office of Research and Development**\nThe term Office of Research and Development means the Office of Research and Development of the Environmental Protection Agency.\n**(17) PFAS terms**\nThe terms perfluoroalkyl substance and polyfluoroalkyl substance have the meanings given those terms in section 7331(2)(B) of the PFAS Act of 2019 ( 15 U.S.C. 8931(2)(B) ).\n**(18) Real-time**\nThe term real-time means the actual or near actual time during which pollutant levels occur at or near the property boundary of a facility or in a nearby community.\n**(19) Source**\nThe term source is within the meaning of the Clean Air Act ( 42 U.S.C. 7401 et seq. ).\n**(20) Test method**\nThe term test method means a method described in the most recent document of the Environmental Protection Agency entitled Compendium of Methods for the Determination of Toxic Organic Compounds in Ambient Air .\n#### 3. Health emergency air toxics monitoring network\n##### (a) Monitoring\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, the Administrator shall publish notice in the Federal Register of, take public comment for a period of not less than 60 days regarding, and take final action to design and launch a plan and implement a program to administer or conduct, pursuant to authority provided under the Clean Air Act ( 42 U.S.C. 7401 et seq. ), including sections 103, 112, 113, 114, and 303 of that Act ( 42 U.S.C. 7403 , 7412, 7413, 7414, 7603), emissions measurement and quantification, including the best available form of fenceline monitoring of stationary sources of hazardous air pollutants that are on the list developed under subsection (c), including through expansion of the National Air Toxics Trends Network or through creating a new network, as appropriate.\n**(2) Monitoring period**\n**(A) In general**\nThe Administrator shall ensure monitoring begins pursuant to this section not later than 18 months after the date of enactment of this Act and shall maintain the monitoring required under paragraph (1) for a period of not less than 6 years after the date on which the monitoring required under that paragraph begins.\n**(B) Subsequent monitoring**\nAfter the 6-year period described in subparagraph (A), the Administrator shall maintain the emissions measurement and quantification program under paragraph (1), consistent with this section, through\u2014\n**(i)**\nmaintaining monitors at all or some sources under the program under paragraph (1); and\n**(ii)**\nadding or moving monitors under the program under paragraph (1) to additional sources, following the process for substitution of sources in subsection (g).\n**(C) Shortened period**\nIf the Administrator determines, after public notice and a public comment period of not less than 60 days, that 6 years of monitoring, as required under subparagraph (A), is not necessary to protect public health or ensure compliance at the source or the facility involved, the Administrator may reduce or end the monitoring after at least 3 years of monitoring has occurred.\n**(D) Additional inspections and testing**\nIn addition to fenceline monitoring under the program under paragraph (1), the Administrator shall use the authority of the Administrator to inspect and require emission testing at sources on the list published pursuant to subsection (c) to the extent necessary to identify and address the emissions crossing the fenceline.\n##### (b) Publication of results\n**(1) In general**\nThe Administrator shall publish and maintain the plans for and the results of all measurements, including fenceline monitoring, conducted under the program under subsection (a)(1) on the website of the Environmental Protection Agency\u2014\n**(A)**\nin a highly accessible format;\n**(B)**\nin a centralized database maintained in multiple languages; and\n**(C)**\nfor a period of at least 10 years.\n**(2) Immediate availability**\nThe Administrator shall ensure that the monitoring data collected under the program under subsection (a)(1) are\u2014\n**(A)**\nelectronically submitted to the Administrator not later than 1 month after the date of collection of the data; and\n**(B)**\nmade publicly available as expeditiously as practicable, but in any case not later than 7 days after the electronic submission of the data.\n##### (c) List of sources\n**(1) Development**\n**(A) In general**\nNot later than 270 days after the date of enactment of this Act, the Administrator shall publish, after public notice and a public comment period of not less than 60 days, a list of stationary sources of hazardous air pollutants that, subject to subparagraph (B) do not already have fenceline monitoring in operation that is producing publicly available data and includes\u2014\n**(i)**\nat least 45 of the sources listed\u2014\n**(I)**\nas high-priority facilities in Appendix A of the report of the Office of Inspector General of the Environmental Protection Agency numbered 20\u2013N\u20130128 and dated March 31, 2020; or\n**(II)**\nas contributing to high cancer risk at the census block level in Appendix C of the report of the Office of Inspector General of the Environmental Protection Agency numbered 21\u2013P\u20130129 and dated May 6, 2021; and\n**(ii)**\nat least 55 other major sources or area sources that meet the criteria described in paragraph (2).\n**(B) Substitution**\n**(i) In general**\nIf the Administrator determines, after public notice and a public comment period of not less than 60 days, that a source described in subparagraph (A)(i) no longer contributes to high health risks or impacts that warrant continued monitoring to advance public health protection, inform improved compliance, or improve available data quality, the Administrator shall\u2014\n**(I)**\ncease to include that source in the list under subparagraph (A); and\n**(II)**\ninclude instead an additional major source or area source described in subparagraph (A)(ii) to ensure that the list under subparagraph (A) includes not fewer than 100 high-priority sources.\n**(ii) Description of reasons**\nFor the purpose of providing notice, the Administrator shall publish in the Federal Register, and seek public comment for a period of not less than 60 days with respect to\u2014\n**(I)**\nany determination to make a substitution under clause (i); and\n**(II)**\nan explanation of the reasons for any such determination demonstrating, based on monitoring data or other reliable information, that the substitution is likely to ensure that monitoring under this section occurs at the sources causing or contributing to the highest potential health risks or other impacts from hazardous air pollution.\n**(iii) Requirement**\nThe Administrator may include an additional major source or area source under clause (i)(II) only if the Administrator determines that the source is, or is likely to be, contributing local health risks or impacts that are equivalent to, or greater than, those of the source for which the new source is being substituted.\n**(2) Criteria**\nThe Administrator may include a major source or area source described in clause (ii) of paragraph (1)(A) on the list described in that paragraph only if the source\u2014\n**(A)**\nemits at least 1 of the pollutants described in paragraph (3);\n**(B)**\nis\u2014\n**(i)**\nlocated in, or within 3 miles of, a census tract with\u2014\n**(I)**\na cancer risk of at least 100-in-1,000,000; or\n**(II)**\na chronic noncancer hazard index that is greater than or equal to 1; or\n**(ii)**\nin a source category with\u2014\n**(I)**\na cancer risk that is greater than 100-in-1,000,000 for the individual most exposed to emissions from the source category;\n**(II)**\na total organ-specific hazard index for chronic noncancer risk that is greater than or equal to 1; or\n**(III)**\nan acute risk hazard quotient that is greater than or equal to 1; and\n**(C)**\n**(i)**\nis classified in 1 or more of North American Industry Classification System codes 322, 324, 325, 326, 331, 332, 339, 424, and 562;\n**(ii)**\n**(I)**\nis required to prepare and implement a risk management plan pursuant to section 112(r) of the Clean Air Act ( 42 U.S.C. 7412(r) ); and\n**(II)**\nhas had an accidental release required to be reported during the previous 5-year period pursuant to sections 68.42 and 68.195 of title 40, Code of Federal Regulations (as in effect on the date of enactment of this Act); or\n**(iii)**\nis determined by the Administrator to be a high-priority source or facility for emissions measurement because\u2014\n**(I)**\nthe facility is located within 350 feet of a residence, school, childcare facility (including a camp), hospital, park, sports or recreation facility, or other gathering place, community center, or institution where children and families regularly spend time; or\n**(II)**\nbased on the best available science, the emissions of the source or facility are likely causing or contributing to, or have the potential to cause or contribute to, serious acute or chronic, including cancer and non-cancer, health or safety risks or impacts, including adverse neurological, developmental, or other health impacts in utero or childhood.\n**(3) Pollutants**\nThe pollutants described in this paragraph are\u2014\n**(A)**\nethylene oxide, CAS 75218;\n**(B)**\nchloroprene, CAS 126998;\n**(C)**\nbenzene, CAS 71432;\n**(D)**\n1,3-butadiene, CAS 106990;\n**(E)**\nformaldehyde, CAS 50000;\n**(F)**\nacetaldehyde, CAS 75070;\n**(G)**\nlead compounds;\n**(H)**\narsenic compounds;\n**(I)**\nantimony compounds;\n**(J)**\ncadmium compounds;\n**(K)**\ncobalt compounds;\n**(L)**\nnickel compounds;\n**(M)**\nmanganese compounds;\n**(N)**\nvinyl chloride;\n**(O)**\nethylene dichloride;\n**(P)**\nnaphthalene;\n**(Q)**\nethylbenzene;\n**(R)**\nmethyl mercury;\n**(S)**\nepichlorohydrin;\n**(T)**\nxylenes;\n**(U)**\nacrylonitrile;\n**(V)**\nany other hazardous air pollutant included in the list described in section 112(b) of the Clean Air Act ( 42 U.S.C. 7412(b) ) that the Administrator determines, after public notice and a public comment period of not less than 60 days, the air emissions of which\u2014\n**(i)**\nare, or may be contributing to, serious health risks; or\n**(ii)**\nwarrant emissions quantification and measurement due to the public interest in evaluating the emissions and effects of the pollutant; and\n**(W)**\nany pollutant or airborne chemical that is a precursor to atmospheric photochemical production of any other pollutant on the list described in section 112(b) of the Clean Air Act ( 42 U.S.C. 7412(b) ).\n**(4) Use of information and methods**\nIn carrying out this subsection, the Administrator shall\u2014\n**(A)**\nuse\u2014\n**(i)**\nthe evaluations and methods of the Environmental Protection Agency for compiling and evaluating information about risks from air toxics in effect on January 1, 2025, that have been peer reviewed by the Science Advisory Board, including chemical assessments developed by the Integrated Risk Information System of the Environmental Protection Agency (commonly referred to as IRIS ), or the most recent Air Toxics Screening Assessment or other current evaluation or report by the Environmental Protection Agency, acting through the Office of Research and Development, providing similar information about cancer and noncancer risks from hazardous air pollution based on measured or modeled emissions, using evaluations or methods that\u2014\n**(I)**\naccount for, and therefore demonstrate higher risks to, the individual or community most exposed to the emissions; and\n**(II)**\naccount for adverse neurological, developmental, or other health impacts in utero, in childhood, and in adolescence;\n**(ii)**\nthe Risk-Screening Environmental Indicators model of the Administrator in effect as of December 31, 2024;\n**(iii)**\na prior health risk assessment that was performed by the Administrator for the applicable source or source category before January 1, 2025; or\n**(iv)**\na new health risk assessment performed by the Administrator for the applicable source or source category that\u2014\n**(I)**\nis more complete and addresses more or greater risks than previously considered;\n**(II)**\nfollows the best available science (including the most recent guidance from the National Academy of Sciences and the most recent assessments under the Integrated Risk Information System of the Environmental Protection Agency (commonly referred to as IRIS ) that were created pursuant to the document of the Environmental Protection Agency entitled ORD Staff Handbook for Developing IRIS Assessments and dated December 2022); and\n**(III)**\nconsiders, with respect to the applicable source or facility\u2014\n**(aa)**\ncumulative risks and cumulative impacts;\n**(bb)**\nincreased vulnerability that results from socioeconomic disparities;\n**(cc)**\nmultiple source exposure; and\n**(dd)**\nexposure in utero, in childhood, in adolescence, and through the age of 85; and\n**(B)**\nconsider\u2014\n**(i)**\nthe most recent emission tests available to the Administrator or received by the Environmental Protection Agency in public comment; and\n**(ii)**\nany fenceline or ambient monitoring data for which an Environmental Protection Agency-approved data quality check has been performed.\n##### (d) Methods and technologies\n**(1) In general**\nExcept as provided in paragraph (3), in carrying out the program under subsection (a)(1), the Administrator shall, for each stationary source on the list published under subsection (c)(1), employ an emissions measurement system to monitor the pollutants described in subsection (c)(3) emitted by the stationary source, including at least\u2014\n**(A)**\nthe most current Environmental Protection Agency-approved or promulgated emission test or monitoring method, including Method 325A, Method 325B, Method TO\u201315A, and Method 327, that expands the scope, strengthens the detection limit, or otherwise improves the effectiveness of the test method; or\n**(B)**\nfor each stationary source described in paragraph (2), the best available method for continuous, real-time measurement of air pollutant concentrations.\n**(2) Stationary sources described**\nA stationary source referred to in paragraph (1)(B) is\u2014\n**(A)**\nnot less than each of the 20 stationary sources on the list published under subsection (c)(1) that\u2014\n**(i)**\nemits the greatest quantity or rate of pollutants described in subsection (c)(3); or\n**(ii)**\ncauses the greatest health risk to the greatest number of people, based on the emissions of the pollutants described in subsection (c)(3) individually, as a group, or cumulatively, based on\u2014\n**(I)**\n**(aa)**\nthe latest evaluations and methods of the Environmental Protection Agency for compiling and evaluating information about risks from air toxics, or the most recent Air Toxics Screening Assessment or other current evaluation or report by the Environmental Protection Agency providing similar information about cancer and noncancer risks from hazardous air pollution based on measured or modeled emissions;\n**(bb)**\nthe Risk-Screening Environmental Indicators model of the Administrator;\n**(cc)**\na prior health risk assessment that was performed by the Administrator for the applicable source or source category; or\n**(dd)**\na new health risk assessment performed by the Administrator that\u2014\n(AA)\nfollows the best available science (including the most recent guidance from the National Academy of Sciences); and\n(BB)\nconsiders, with respect to the applicable source or facility, cumulative risks and impacts, increased vulnerability that results from socioeconomic disparities, multiple source exposure, and exposure in utero, in childhood, in adolescence, and over the course of a lifetime through the age of 85; and\n**(II)**\nthe most recent emission tests available to the Environmental Protection Agency or received in public comment, and any fenceline or ambient monitoring data for which an Environmental Protection Agency-approved data quality check has been performed;\n**(B)**\nany other stationary source on the list published under subsection (c)(1) that\u2014\n**(i)**\nis regulated under paragraph (7) of section 112(r) of the Clean Air Act ( 42 U.S.C. 7412(r) ); and\n**(ii)**\nhas had an accidental release or incident that is required to be reported during the previous 5-year period pursuant to sections 68.42 and 68.195 of title 40, Code of Federal Regulations (as in effect on January 1, 2025), under that paragraph; and\n**(C)**\nany other stationary source on the list published under subsection (c)(1) for which application of the methods described in subparagraph (A) alone may not be sufficient\u2014\n**(i)**\nto monitor and report the pollutants described in subsection (c)(3) that are emitted by that stationary source; or\n**(ii)**\nto advance public health and safety.\n**(3) Updates**\n**(A) Approved or promulgated methods**\nThe Administrator shall\u2014\n**(i)**\nnot later than 2 years after the date of enactment of this Act, review and, after public notice and a public comment period of not less than 60 days, update each approved or promulgated test method described in this section to add as many of the pollutants described in subsection (c)(3) as practicable; and\n**(ii)**\notherwise strengthen the test methods described in clause (i) to support effective hazardous air pollutant measurement and the full implementation of this Act.\n**(B) New test methods**\n**(i) In general**\nNot later than 18 months after the date of enactment of this Act, the Administrator shall, after public notice and a public comment period of not less than 60 days, approve or promulgate, as applicable, any new test methods that are necessary to ensure effective fenceline monitoring of all pollutants and sources described in this section, including\u2014\n**(I)**\nat least 1 method that represents the best and most accurate form of continuous, real-time fenceline monitoring based on the best available science; and\n**(II)**\nat least 1 method that represents the best and most accurate form of multimetal monitoring based on the best available science.\n**(ii) Updates required**\nNot less frequently than once every 6 years, the Administrator shall review and, if necessary, after public notice and a public comment period of not less than 60 days, strengthen or add new test methods that meet the requirements under clause (i), which shall be based on\u2014\n**(I)**\nthe best available monitoring technologies that improve the quality or quantity of information provided by, or improve the precision or other type of scientific reliability of, a method; and\n**(II)**\nthe advice of staff of the Office of Enforcement and Compliance, staff of the Office of Research and Development, regional or other staff within the Environmental Protection Agency responsible for, and with expertise on, the enforcement of this Act, and other monitoring experts.\n**(4) Office of Research and Development**\nThe Administrator shall act through the Assistant Administrator for Research and Development, and in coordination with the Assistant Administrator for Air and Radiation, to carry out this subsection.\n##### (e) Monitor placement and maintenance\n**(1) In general**\nThe Administrator shall, after public notice and a public comment period of not less than 60 days with respect to monitor placement and maintenance plans, place and maintain, or ensure placement and regular maintenance of, all monitors required under this section to ensure effective and reliable emissions measurement pursuant to this section.\n**(2) Maintenance check**\nThe maintenance required under paragraph (1) shall include a maintenance check of the monitor not less frequently than once every 180 days, unless\u2014\n**(A)**\nthe test method used by the monitor requires a maintenance check more frequently; or\n**(B)**\na maintenance check is requested by a member of the public.\n**(3) Public input**\nThe Administrator shall, after public notice and a public comment period of not less than 60 days, create a process, including an accessible online resource or website, for the public\u2014\n**(A)**\nto track the maintenance of monitors under this subsection; and\n**(B)**\nto request a maintenance check of a monitor.\n##### (f) Report\nNot later than 6 years after the date of enactment of this Act, and not less frequently than once every 6 years thereafter, the Administrator shall submit to Congress and post publicly on the website of the Environmental Protection Agency a report describing the results of the program carried out under subsection (a)(1), which shall include\u2014\n**(1)**\nthe results of emissions measurement implemented under that program;\n**(2)**\nany actions of the Administrator taken based on that emissions measurement data or program; and\n**(3)**\nwhether the Administrator proposes\u2014\n**(A)**\nto continue emissions measurements at any or all of the stationary sources on the list published under subsection (c)(1); or\n**(B)**\nto implement emissions measurements of any additional stationary sources as determined under subsection (g).\n##### (g) Determination regarding additional sources\nNot later than 6 years after the date of enactment of this Act, and not less frequently than once every 6 years thereafter, the Administrator shall\u2014\n**(1)**\nafter public notice and a public comment period of not less than 60 days, make a determination of whether to add or remove sources to the list published under subsection (c)(1)\u2014\n**(A)**\nto ensure compliance of those stationary sources with existing emission standards under section 112 of the Clean Air Act ( 42 U.S.C. 7412 );\n**(B)**\nto prevent and detect accidental releases;\n**(C)**\nto protect the health of the communities, including children and other vulnerable populations, most exposed to the emissions of hazardous air pollutants from such stationary sources to the maximum extent practicable; or\n**(D)**\nto ensure the 100 highest-priority sources or facilities, based on the best available science and the most current data on health risks and impacts (including the most current research on children\u2019s health), have emissions measurement systems in place for pollutants required to be monitored under this section; and\n**(2)**\npublish a determination under paragraph (1) in the Federal Register.\n##### (h) Report\nNot later than 1 year after the date of enactment of this Act, the Administrator shall submit to Congress and make publicly available online a report that\u2014\n**(1)**\ndescribes the staffing that is available, necessary, and planned to carry out this section; and\n**(2)**\ndemonstrates how the Administrator intends to carry out the duties and requirements of this section without impact or delay on any other duty or responsibility of the Administrator.\n##### (i) No exemption authority\nNo exemption from compliance with any standard or limitation under this section may be issued pursuant to section 112(i)(4) of the Clean Air Act ( 42 U.S.C. 7412(i)(4) ) to any stationary source.\n##### (j) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $146,000,000 for the period of fiscal years 2026 and 2027.\n#### 4. Community air toxics monitoring\n##### (a) Regulations\nNot later than 2 years after the date of enactment of this Act, the Administrator shall promulgate regulations pursuant to authority provided by the Clean Air Act, which may include section 103, subsections (d), (f), and (r) of section 112, section 113, and section 114 of that Act ( 42 U.S.C. 7403 , 7412, 7413, 7414), for each source category described in subsection (b), that\u2014\n**(1)**\nrequire all sources in the source category to implement, not later than 1 year after the promulgation of the regulations, the best available form of emissions measurement, including continuous emissions monitoring and fenceline monitoring, to ensure compliance with the emission standards for hazardous air pollutants;\n**(2)**\nfor facilities in the source category that are required to submit risk management plans under section 112(r)(7) of that Act ( 42 U.S.C. 7412(r)(7) ), require each facility to implement\u2014\n**(A)**\ncontinuous, real-time monitoring to provide for effective emergency response and provide information to prevent future releases; and\n**(B)**\nemissions measurement, including fenceline monitoring, to provide for effective emergency response and provide information to prevent future releases;\n**(3)**\nsubject to subsection (e)\u2014\n**(A)**\nestablish a corrective action level at the fenceline for at least the top 5 hazardous air pollutants that drive the cancer, chronic noncancer, or acute risk for the source category; and\n**(B)**\nrequire corrective action for the release of any quantity of a substance listed pursuant to section 112(r)(3) of that Act ( 42 U.S.C. 7412(r)(3) );\n**(4)**\nif any applicable corrective action level under paragraph (3)(A) is exceeded, require\u2014\n**(A)**\na root cause analysis and preventive action report;\n**(B)**\nfull remedial action, including implementation of all control technologies, practices, processes, operational improvements, or other measures necessary to resolve the exceedance and protect the most exposed or most vulnerable individuals potentially affected by the exceedance (including children) and to make best efforts to prevent the exceedance from recurring, based on and applying input from the most affected individuals and communities; and\n**(C)**\na public report that\u2014\n**(i)**\ndescribes\u2014\n**(I)**\nthe results of the root cause analysis and preventive action report under subparagraph (A); and\n**(II)**\nthe remedial actions taken under subparagraph (B); and\n**(ii)**\ncertifies that a violation of the Clean Air Act ( 42 U.S.C. 7401 et seq. ) has occurred; and\n**(5)**\ntreat any requirement imposed by the regulations under this section as a requirement under section 112 of the Clean Air Act ( 42 U.S.C. 7412 ) that is enforceable under section 113 of that Act ( 42 U.S.C. 7413 ).\n##### (b) Source categories\nThe source categories described in this subsection include\u2014\n**(1)**\neach category or subcategory of major sources or area sources that\u2014\n**(A)**\ncontains\u2014\n**(i)**\nat least 1 of the stationary sources of hazardous air pollutants that are on the list published under section 3(c);\n**(ii)**\nmajor sources or area sources identified in the most recent National Emissions Inventory of the Environmental Protection Agency as emitting a pollutant described in section 3(c)(3);\n**(iii)**\npetroleum, chemical, petrochemical, or plastics manufacturing sources, marine vessel loading operations, or other sources that are classified in 1 or more of North American Industry Classification System codes 322, 324, 325, 326, 331, 332, 339, 424, and 562; or\n**(iv)**\nany other major source or area source of fugitive hazardous air pollutant emissions for which the Environmental Protection Agency is subject to a court-ordered or statutory deadline, engaged in a reconsideration proceeding, or subject to a court remand (or is likely within the 2-year period beginning on the date of enactment of this Act to become subject to such an obligation or action) to review and determine whether to revise the emissions standards that apply to that source category; or\n**(B)**\ncontains any stationary source that\u2014\n**(i)**\nis regulated under paragraph (7) of section 112(r) of the Clean Air Act ( 42 U.S.C. 7412(r) ); and\n**(ii)**\nhas had an accidental release or incident that is required to be reported during the previous 5-year period under that section and the regulations thereunder that were in effect as of January 1, 2025; and\n**(2)**\nany other source category for which the Administrator determines that requiring fenceline monitoring is likely to benefit public health or welfare, including children\u2019s health, based on the best available science.\n##### (c) Determination of best available form of monitoring\n**(1) In general**\nThe Administrator, in consultation with the Office of Air and Radiation, the Office of Enforcement and Compliance Assurance, the Office of Environmental Justice and External Civil Rights, the Office of Children\u2019s Health, and the Office of Research and Development, shall, for purposes of the regulations promulgated pursuant to subsection (a)\u2014\n**(A)**\ndetermine the best available form of emissions measurement, including continuous emissions monitoring and fenceline monitoring; and\n**(B)**\nensure the methods required under the regulations are at least as stringent as the most current Environmental Protection Agency-approved or promulgated emission test or monitoring method, including Method 325A, Method 325B, Method 327, and Method TO\u201315A.\n**(2) Requirement**\nIn carrying out paragraph (1)(B), the Administrator shall ensure that 1 or more of the methods described in or promulgated under section 3 or subsection (d) (including multimetal monitoring) is included in the regulations promulgated pursuant to subsection (a) if that method is the best available method for 1 or more of the pollutants for which monitoring is required under this section.\n##### (d) Methods and technologies\n**(1) In general**\nFor all stationary sources in the source categories described in subsection (b), as the best available fenceline monitoring method for those source categories, the Administrator may, in the regulations promulgated pursuant to subsection (a)\u2014\n**(A)**\nrequire application, implementation, or employment of optical remote sensing technology to provide real-time measurements of air pollutant concentrations along an open-path; or\n**(B)**\nprovide an explanation of why application, implementation, or employment of 1 or more of the technologies described in subparagraph (A) is not necessary\u2014\n**(i)**\nto ensure compliance with the emission standards established under the regulations promulgated pursuant to subsection (d), (f), or (r) of section 112 of the Clean Air Act ( 42 U.S.C. 7412 ), as applicable; or\n**(ii)**\nto protect the public health, to prevent accidental releases, or to provide for effective emergency response.\n**(2) Multiple-source or facility complexes**\n**(A) Definition of multiple-source or facility complex**\nIn this paragraph, the term multiple-source or facility complex means 1 or more stationary sources co-located at the same site.\n**(B) Multiple-source or facility complex monitoring**\nIn the regulations promulgated pursuant to subsection (a), the Administrator shall ensure that the best available form of monitoring for a multiple-source or facility complex that contains not less than 2 stationary sources in 1 or more of North American Industry Classification System codes 324, 325, and 326, or a related chemical or petrochemical sector, is at least a combination of\u2014\n**(i)**\nreal-time, open-path monitoring; and\n**(ii)**\nMethod 325A, Method 325B, and Method 327, as applicable depending on the types of emissions to be measured.\n**(C) Requirement**\nIn carrying out subparagraph (B), the Administrator shall consider whether any other multiple-source or facility complexes should be required to employ the combined monitoring methods described in that subparagraph.\n##### (e) Health priority approach\nIn promulgating the corrective action level for each of the hazardous air pollutants described in subsection (a)(3)(A), the Administrator shall\u2014\n**(1)**\nconsider the best available science, including applying the most health-protective approach possible and applying a precautionary approach to account for uncertainty;\n**(2)**\nensure that the owner or operator of the source or facility reduces the emissions of the source or facility to prevent harm if the measured concentration at the fenceline would, or is likely to\u2014\n**(A)**\nincrease harm to public health or safety (including through an increased health risk to any individual, including a child); or\n**(B)**\nreach a level that may result in short-term, long-term, or chronic human exposure to air pollution (including any exposure that begins in utero, infancy, childhood, or adolescence) that increases the risk of\u2014\n**(i)**\nhealth harms resulting from odors, irritation, sensitizing effects, or any combination of those harms;\n**(ii)**\na chronic condition (including neurodevelopmental) or disease (including cancer and other illnesses); or\n**(iii)**\ndeath; and\n**(3)**\ntake into account the aggregate and cumulative emissions and health risks from the facility, including multiple source categories, as applicable, to ensure full health protection from the entire facility based on the best available science.\n##### (f) Maintenance and public reporting\n**(1) In general**\nIn the regulations promulgated pursuant to subsection (a), the Administrator shall ensure that\u2014\n**(A)**\nthe owners or operators of sources subject to the requirements of this section\u2014\n**(i)**\nperform regular inspections and maintenance of all measured equipment required under this section; and\n**(ii)**\nsubmit to the Administrator regular reports that\u2014\n**(I)**\ninclude the measured emissions data collected by that emissions measurement equipment;\n**(II)**\ndescribe the status of that measurement equipment; and\n**(III)**\ncontain a detailed explanation of the circumstances surrounding a delay in collecting or missing data;\n**(B)**\nthe emissions measurement system required under this section is continuous and yields reliable data not less than 95 percent of the time, without any regulatory exemption or extension; and\n**(C)**\nany problem with the fenceline monitoring equipment required under this section is repaired within 2 days of discovering the problem.\n**(2) Violation**\nIn the regulations promulgated pursuant to subsection (a), the Administrator shall\u2014\n**(A)**\nrequire the owner or operator of a stationary source subject to such regulations to report, with respect to the source, at least semiannually\u2014\n**(i)**\nall exceedances of any corrective action level; and\n**(ii)**\nall corrective action planned and taken; and\n**(B)**\nfor purposes of imposing penalties, treat each day on which a violation of a reporting requirement under subparagraph (A) continues as a separate violation.\n**(3) Public reporting**\n**(A) In general**\nThe Administrator shall make available on the website of the Environmental Protection Agency, in an accessible format that includes multiple languages spoken by residents living near the source where monitoring was conducted\u2014\n**(i)**\nall emissions measurement plans, reports, and other information collected or required under this section;\n**(ii)**\nall emissions measurement data collected by monitoring equipment required under this section; and\n**(iii)**\nan option to sign up for community-wide or source-specific alerts that alert the user if the emissions concentrations measured pursuant to clause (i) or (ii), as applicable, exceed\u2014\n**(I)**\na health reference level of the Administrator that has been scientifically peer-reviewed;\n**(II)**\na health reference level approved by the Administrator that has been scientifically peer-reviewed;\n**(III)**\na health reference level approved by any State or Tribal government that has been scientifically peer-reviewed; or\n**(IV)**\nthe applicable corrective action level under subsection (a)(3)(A).\n**(B) Public notice and comment**\nThe Administrator shall provide notice and receive public comment for not less than 60 days on the format and accessibility of the information required to be made available under subparagraph (A).\n**(C) Publication**\nThe Administrator shall publicize the information required to be made available under subparagraph (A) in each community that contains a source regulated under this section through not less than 2 of the most widely viewed local media formats for members of that community that live nearest the regulated source.\n##### (g) Office of Research and Development\nThe Administrator shall ensure that the Assistant Administrator for Air and Radiation coordinates with the Assistant Administrator for Research and Development, as well as any other appropriate offices of the Environmental Protection Agency, to carry out this section.\n##### (h) Report\nNot later than 1 year after the date of enactment of this Act, the Administrator shall submit to Congress and make publicly available online a report that\u2014\n**(1)**\ndescribes the staffing that is available, necessary, and planned to carry out this section; and\n**(2)**\ndemonstrates how the Administrator intends to carry out the duties and requirements of this section without impact or delay on any other duty or responsibility of the Administrator.\n##### (i) No exemption authority\nNo exemption from compliance with any standard or limitation under this section may be issued pursuant to section 112(i)(4) of the Clean Air Act ( 42 U.S.C. 7412(i)(4) ) to any stationary source.\n##### (j) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $50,000,000 for the period of fiscal years 2026 and 2027.\n#### 5. NAAQS monitoring network\n##### (a) Deployment of NCore multipollutant monitoring stations\n**(1) In general**\nThe Administrator shall require the deployment of 80 additional NCore multipollutant monitoring stations.\n**(2) Requirement**\nAll monitors at the stations required to be deployed pursuant to paragraph (1) that measure pollutants for which the Administrator has established national ambient air quality standards shall\u2014\n**(A)**\nbe Federal reference method or Federal equivalent method monitors; and\n**(B)**\nproduce monitoring data that are sufficient for determining whether the relevant national ambient air quality standard is met at the site.\n##### (b) Deadline\nNot later than 18 months after the date of enactment of this Act, the Administrator shall ensure that all NCore multipollutant monitoring stations required to be deployed under subsection (a)(1) are\u2014\n**(1)**\ninstalled and integrated into the air quality monitoring system established pursuant to sections 110(a)(2)(B) and 319 of the Clean Air Act ( 42 U.S.C. 7410(a)(2)(B) , 7619); and\n**(2)**\nafter installation, operated and maintained on a continuing basis.\n##### (c) Monitoring results\nMonitoring results from NCore multipollutant stations required to be deployed under subsection (a)(1) shall be used for\u2014\n**(1)**\nassessments of the compliance of areas with national ambient air quality standards;\n**(2)**\nintegrated science assessments in reviews of national ambient air quality standards established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 );\n**(3)**\nevaluating disparities of pollution exposures within metropolitan areas; and\n**(4)**\nsuch other purposes as the Administrator determines will promote the protection of public health from air pollution.\n##### (d) Locations\n**(1) Vulnerable populations**\n**(A) In general**\nThe Administrator shall ensure that not fewer than 40 of the NCore multipollutant monitoring stations required to be deployed under subsection (a)(1)\u2014\n**(i)**\nare not limited to metropolitan statistical areas with populations of 50,000 or greater; and\n**(ii)**\nmeet the requirement described in subparagraph (B).\n**(B) Requirement described**\nThe requirement referred to in subparagraph (A)(ii) is that the NCore multipollutant monitoring stations shall be sited in census tracts that each meet 1 or more of the following criteria, with the specific site selected consistent with Appendix D to part 58 of title 40, Code of Federal Regulations (as in effect on the date of enactment of this Act), except that where the provisions of this Act conflict with that appendix, the provisions of this Act shall control:\n**(i)**\nThe rates of childhood asthma, adult asthma, chronic obstructive pulmonary disease, heart disease, or cancer are not less than 5 percent higher than the national average for that condition in the census tract.\n**(ii)**\nThe percentage of people living below the poverty level, that are above age 18 without a high school diploma, or that are unemployed, is higher than the national average in the census tract.\n**(iii)**\n2 or more major sources (as defined in section 501 of the Clean Air Act ( 42 U.S.C. 7661 )) are located within the census tract or adjacent census tracts combined.\n**(iv)**\nThere is a higher-than-national-average population in the census tract of vulnerable or sensitive individuals who may be at greater risk than the general population of adverse health effects from exposure to 1 or more air pollutants for which national ambient air quality standards have been established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ).\n**(2) Siting determinations**\nIn determining and approving sites for NCore multipollutant monitoring stations required to be deployed under subsection (a)(1), the Administrator shall\u2014\n**(A)**\ninvite proposals from or on behalf of residents of any community for the siting of the stations in that community, which may include inviting proposals through regional or virtual meetings;\n**(B)**\nprioritize siting of the stations in census tracts or counties based on\u2014\n**(i)**\nthe potential for the levels of 1 or more air pollutants to be monitored by the stations to reach or exceed the level of the applicable national ambient air quality standard established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ), including evidence of relevant industrial activity or nearby exceedances;\n**(ii)**\nthe number of people who live, work, attend school, or recreate in the area or areas for which monitoring by the stations is reasonably anticipated to be representative with respect to air quality and the proportion of those people who are at higher risk than the general population of adverse health effects from the air pollutants monitored;\n**(iii)**\nthe lack or inadequacy of existing air quality monitors for providing representative air quality data for the affected area or areas for the pollutants to be measured by the station; and\n**(iv)**\nthe current designation of the area in which the monitoring station would be located as unclassifiable or in attainment for 1 or more of the pollutants to be monitored by that station; and\n**(C)**\nprior to making siting determinations\u2014\n**(i)**\nhold at least 1 public hearing in or near each proposed siting location;\n**(ii)**\nprovide public notice of the proposed siting locations and the hearings required under clause (i)\u2014\n**(I)**\nin the Federal Register;\n**(II)**\nby email to persons who have requested notice of proposed siting determinations;\n**(III)**\nby news release; and\n**(IV)**\nby posting on the public website of the Environmental Protection Agency;\n**(iii)**\nprovide an opportunity for public comment for not less than 60 days after the date of publication of the notice required under clause (ii) in the Federal Register; and\n**(iv)**\npublish online an explanation and record for the siting decisions of the Administrator.\n**(3) Reliance on hybrid methods**\nIn determining under paragraph (2)(B)(i) the potential for an air pollutant to reach or exceed the level of the applicable standard, the Administrator may rely on hybrid methods that combine information from multiple sources, including monitors, sensors, modeling, and satellites.\n##### (e) Additional ambient monitors\n**(1) In general**\nThe Administrator shall deploy not fewer than 100 additional Federal reference method monitors or Federal equivalent method monitors for 1 or more air pollutants for which national ambient air quality standards have been established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ) in areas\u2014\n**(A)**\nthat are unmonitored or undermonitored, as determined by the Administrator; and\n**(B)**\nwithin which the Administrator determines, after public notice and comment, that adding those monitors is warranted\u2014\n**(i)**\nto detect whether the area is in nonattainment of the applicable national ambient air quality standards; and\n**(ii)**\nto improve the publicly available data on air quality for 1 or more of those air pollutants (or precursors to those air pollutants).\n**(2) Siting determinations**\nIn approving sites for new Federal reference method monitors or Federal equivalent method monitors required under this subsection, the Administrator shall prioritize siting of the stations in census tracts or counties in accordance with subsection (d)(2)(B).\n**(3) Relation to previously deployed or planned monitors**\nThe Federal reference method monitors required under this subsection shall be in addition to, and not in lieu of, any monitors already deployed or planned for deployment by the Administrator, any State, any other governmental entity, or any other entity prior to the date of enactment of this Act.\n##### (f) Report\nNot later than 2 years after the date of enactment of this Act, the Administrator shall\u2014\n**(1)**\nin coordination with the States, complete an assessment, which includes public input, on the status of all ambient air quality monitors that are part of Federal, State, or local networks and used for determining compliance with national ambient air quality standards, which shall identify\u2014\n**(A)**\neach monitor that is not operating properly and that needs to be repaired or replaced; and\n**(B)**\neach monitor that is past the end of its ordinary useful life; and\n**(2)**\nsubmit to Congress and make available on the public website of the Environmental Protection Agency a report that includes\u2014\n**(A)**\na list of all monitors identified under paragraph (1); and\n**(B)**\na schedule and plan to restore to proper operation or replace all monitors included in the list under paragraph (1)(A) and to replace all monitors included on the list under paragraph (1)(B), with all restorations and replacements to be completed not later than 40 months after the date of enactment of this Act, except that the schedule and plan shall not apply to monitors\u2014\n**(i)**\nthat have been discontinued in accordance with section 58.14(c) of title 40, Code of Federal Regulations (as in effect on the date of enactment of this Act); and\n**(ii)**\n**(I)**\nfor which such discontinuation is not subject to a judicial challenge; or\n**(II)**\nfor which a judicial challenge described in subclause (I) has been fully resolved by a settlement or order that authorizes discontinuation of the monitor.\n##### (g) Designations\nNot later than 2 years after the date on which data are received from a monitor sited pursuant to this section that demonstrate that an area designated by the Administrator pursuant to paragraph (1) of section 107(d) of the Clean Air Act ( 42 U.S.C. 7407(d) ) as in attainment or unclassifiable for an air pollutant is not meeting or is contributing to air quality in a nearby area that does not meet 1 or more applicable national ambient air quality standards, the Administrator shall redesignate pursuant to paragraph (3) of that section that area as in nonattainment for that pollutant unless the designation is otherwise precluded under this Act.\n##### (h) Satellite monitoring\n**(1) Definition of design value**\nIn this subsection, the term design value means, for each pollutant, the air quality statistic the Administrator defines in part 50 (including appendices) of title 40, Code of Federal Regulations (as in effect on the date of enactment of this Act), for comparison with the relevant national ambient air quality standard established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ), regardless of whether the regulation (including appendices) in part 50 of title 40, Code of Federal Regulations (as in effect on the date of enactment of this Act), uses the term design value .\n**(2) Satellite monitoring data**\n**(A) Provision of satellite data**\nThe Administrator shall consult with the Administrator of the National Aeronautics and Space Administration on methods to facilitate the use of data from the satellites of the National Aeronautics and Space Administration or other entities for use in calculating design values under any national ambient air quality standards for PM 10 , PM 2.5 , ozone, and oxides of nitrogen for purposes of determining compliance or noncompliance with the national ambient air quality standards for those pollutants.\n**(B) Regulations required**\nNot later than 18 months after the date of enactment of this Act, the Administrator shall, after public notice in the Federal Register and a public comment period of not less than 60 days, promulgate regulations to specify procedures (including any modeling techniques) for using data described in subparagraph (A) in combination with information from multiple sources, including monitors and modeling, to calculate the expected number of exceedances per year and the design values for PM 10 , PM 2.5 , ozone, and oxides of nitrogen for purposes of determining compliance or noncompliance with the national ambient air quality standards for those pollutants.\n**(3) National Academy of Sciences report**\n**(A) In general**\nThe Administrator may enter into an arrangement with the National Academy of Sciences under which the National Academy of Sciences agrees to submit a report that describes the actions necessary, including new science and satellite assets, to enable the contribution of satellite monitoring to the calculation of design values and nonattainment determinations under any national ambient air quality standards for ozone and oxides of sulfur established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ).\n**(B) Regulations required**\n**(i) In general**\nNot later than 18 months after the date of enactment of this Act, the Administrator, in coordination with the Administrator of the National Aeronautics and Space Administration and the Administrator of the National Oceanic and Atmospheric Administration, shall, after public notice in the Federal Register and a public comment period of not less than 60 days, promulgate regulations that provide a plan for the use of satellite monitoring data in calculating design values for the pollutants described in subparagraph (A).\n**(ii) Requirement**\nNot later than January 1, 2028, the Administrator shall implement the plan required by clause (i) and provide for use of satellite data in calculating design values for the pollutants described in subparagraph (A).\n##### (i) Monitoring plans\nNotwithstanding any other provision of law, the Administrator may not approve a State monitoring plan under section 58.10 of title 40, Code of Federal Regulations (or successor regulations), unless\u2014\n**(1)**\nthe State provided, with respect to the State monitoring plan\u2014\n**(A)**\npublic notice of the proposal of the plan in a highly accessible format in multiple languages, including a publicly accessible web page address where members of the public can at any time view the entire proposed plan and supporting materials;\n**(B)**\nnot less than 45 days for public comment; and\n**(C)**\nan opportunity for public hearing; and\n**(2)**\nthe Administrator\u2014\n**(A)**\nproposes in the Federal Register to approve or disapprove of the State monitoring plan;\n**(B)**\nprovides not less than 45 days for public comment on the proposal described in subparagraph (A); and\n**(C)**\nafter consideration of any comments received pursuant to subparagraph (B), publishes in the Federal Register the final action on the proposal described in subparagraph (A).\n##### (j) Funding\n**(1) Authorization of appropriations**\nThere is authorized to be appropriated to carry out this section $75,000,000 for fiscal year 2026.\n**(2) Uses**\nThe Administrator\u2014\n**(A)**\nmay use the amounts made available to carry out this section\u2014\n**(i)**\nto directly deploy new or replacement NCore multipollutant monitoring stations required to be deployed under subsection (a)(1); or\n**(ii)**\nto make grants under section 103 or 105 of the Clean Air Act ( 42 U.S.C. 7403 , 7405) to State and local governments for deployment and operation of the NCore multipollutant monitoring stations required to be deployed under subsection (a)(1); and\n**(B)**\nshall use not less than 5 percent, but not more than 10 percent, of the amounts made available to carry out this section to perform the maintenance and repairs necessary to restore to operation NCore multipollutant monitoring stations that are\u2014\n**(i)**\nas of the date of enactment of this Act, nonoperational; and\n**(ii)**\nlocated in areas that are designated as in nonattainment of national ambient air quality standards established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ) for ozone or particulate matter.\n#### 6. Community air quality system monitoring\n##### (a) Deployment of air quality systems\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Administrator\u2014\n**(A)**\nshall deploy, in accordance with the prioritization criteria described in section 5(d)(2), not fewer than 1,000 air quality systems, each of which shall cost not more than $5,000;\n**(B)**\nshall deploy those air quality systems in clusters of not fewer than 5 in each of the census tracts or counties selected;\n**(C)**\nbefore determining and approving sites for those air quality systems, shall invite, through public notice and other means designed to reach communities disproportionately impacted by air pollution, proposals from or on behalf of residents of any community for the sites;\n**(D)**\nmay contract with nonprofit organizations (including academic institutions) and State and local air pollution control agencies to conduct air quality system monitoring and report the results; and\n**(E)**\nshall make data from air quality systems installed pursuant to this section public on an easily accessible data platform.\n**(2) Requirement**\nIn carrying out paragraph (1), the Administrator shall select systems for deployment that\u2014\n**(A)**\nare available on the market at the time of purchase;\n**(B)**\nthe Administrator determines will provide data of sufficient accuracy to provide a reasonable basis for determining whether the location in which the air quality system is sited is or may be at risk of exceeding 1 or more national ambient air quality standards established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ); and\n**(C)**\nare the lowest cost available that meet the standards described in subparagraph (B).\n**(3) Exception to cost limitation**\nNotwithstanding paragraph (1), if the Administrator determines in writing that a system to measure a particular pollutant is not available on the market at a price at or below $5,000 each, the Administrator may spend an amount above $5,000 to acquire that system so long as the Administrator complies with subparagraphs (B) and (C) of paragraph (2).\n##### (b) Pollutants\n**(1) In general**\n**(A) List**\nNot fewer than 500 air quality systems deployed pursuant to subsection (a) shall measure 1 or more of the following pollutants:\n**(i)**\nOzone.\n**(ii)**\nPM 2.5 .\n**(iii)**\nOxides of nitrogen.\n**(iv)**\nSulfur dioxide.\n**(B) Required sensors**\nAll air quality systems deployed pursuant to subsection (a) may include sensors to measure wind speed, wind direction, relative humidity, carbon dioxide and carbon monoxide, and other inputs that aid with source identification.\n**(2) Determination**\nThe Administrator shall determine which air pollutant or air pollutants an air quality system deployed pursuant to subsection (a) shall monitor based on the pollution sources affecting the area in which the air quality system is to be deployed.\n##### (c) Determination and installation\n**(1) In general**\nNot later than 18 months after the date on which an air quality system deployed pursuant to subsection (a) has been monitoring air quality data for 1 year, the Administrator shall determine whether the air quality systems deployed in the applicable census tract or county reported air pollution levels over the 1-year period ending on the date of the determination that reached or exceeded 98 percent of the level of any applicable national ambient air quality standard established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ) for any air pollutant.\n**(2) Requirement**\nIf the Administrator makes a determination under paragraph (1) that an air pollutant described in subsection (b)(1) met or exceeded the threshold described in that paragraph, the Administrator shall, not later 180 days after the date of the determination, ensure that Federal reference method monitors or Federal equivalent method monitors are installed and in operation within that census tract or county for each pollutant that met or exceeded the threshold.\n**(3) Exceptions**\nThe Administrator shall waive the requirement of paragraph (2) if the Administrator finds, within the 180-day period described in that paragraph, and after providing notice and an opportunity for public comment, that based on clear and convincing evidence\u2014\n**(A)**\nthe measurements from the systems supporting the determination described in paragraph (2) were so inaccurate as to provide no reasonable basis for finding that levels of the relevant pollutant reached 98 percent of the level of the national ambient air quality standard established under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ) for the relevant pollutant; or\n**(B)**\ncomplementary data, such as information on the ambient matric, meteorology, measurements from other nearby systems or ambient monitors, modeling, satellite data, or other relevant and reliable information, demonstrate that levels of the relevant pollutant could not have plausibly reached 98 percent of the level of that standard.\n##### (d) Report\nNot later than 1 year after the date of enactment of this Act, and after public notice and a public comment period of not less than 60 days, the Administrator shall make publicly available online a report describing additional areas in which data from low-cost air quality systems may be relevant or useful for decisionmaking or for the purpose of increasing public access to information.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $6,000,000 for fiscal year 2026.\n#### 7. Hazardous air pollutant monitoring\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, for the purposes of improving the quality of the national emissions inventory and advancing public access to information, the Administrator shall, after public notice and a public comment period of not less than 60 days, amend subpart A of part 51 of title 40, Code of Federal Regulations, to update and expand the requirements under that subpart to require all major and non-major sources to report additional emissions data, including emissions of hazardous air pollutants, perfluoroalkyl substances, and polyfluoroalkyl substances.\n##### (b) Minimum requirements\nThe amendment required under subsection (a) shall, at a minimum\u2014\n**(1)**\ncontain all amendments described in the proposed rule of the Environmental Protection Agency entitled Revisions to the Air Emissions Reporting Requirements (88 Fed. Reg. 54118 (August 9, 2023));\n**(2)**\nensure reporting of emissions during periods of malfunction of the source; and\n**(3)**\nconsistent with the proposal to require reporting of emissions of perfluoroalkyl substances and polyfluoroalkyl substances in the rule described in paragraph (1), require, in the reporting cycle immediately following the date on which a pollutant is listed as a hazardous air pollutant, the reporting of emissions of that pollutant.\n##### (c) Effective date\nThe amendment required under subsection (a) shall take effect for the first inventory year that begins after that amendment is finalized.\n#### 8. Data requirement\nTo the extent practicable, the Administrator shall\u2014\n**(1)**\n**(A)**\nrestore for public access the EJSCREEN mapping tool of the Environmental Protection Agency; or\n**(B)**\ncreate a relevant, nationwide geospatial mapping and screening tool similar to and providing, at minimum, all of the data previously included in the EJSCREEN mapping tool that the Administrator, acting through the Assistant Administrator for Research and Development, shall make available online for public comment not later than 270 days after the date of enactment of this Act; and\n**(2)**\nintegrate into the applicable tool restored or created under paragraph (1) the data collected through the programs established under this Act.\n#### 9. Rule of construction\nNothing in this Act amends any other statute or revises or alters any duty or authority of the Administrator under any other applicable law.",
      "versionDate": "2025-12-17",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-12-17",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "3529",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Public Health Air Quality Act of 2025",
      "type": "S"
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-22T15:12:59Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6782ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Public Health Air Quality Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Health Air Quality Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect clean air and public health by expanding fenceline and ambient air monitoring and access to air quality information for communities affected by air pollution, to require hazardous air pollutant monitoring at the fenceline of facilities whose emissions are linked to local health threats, to ensure the Environmental Protection Agency promulgates rules that require hazardous air pollutant data measurement and electronic submission at fencelines and stacks of industrial source categories, to expand and strengthen the national ambient air quality monitoring network, to deploy air quality systems in communities affected by air pollution, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:34Z"
    }
  ]
}
```
